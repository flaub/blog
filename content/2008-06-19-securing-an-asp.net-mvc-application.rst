Securing an ASP.NET MVC Application
###################################

Authorization Manager
---------------------

Authorization Manager (aka AzMan) is a set of COM objects that come with Windows
Server 2003 to provide applications with the ability to define security
policies. You can install this and other tools in your development environment
by doing the following:

 #. Download the `Windows Server 2003 SP1 Administration Tools Pack`_
 #. Install the Windows Server 2003 SP1 Administration Tools Pack
 
    - Run WindowsServer2003-KB304718-AdministrationToolsPack.exe
    - Next
    - I Agree, Next
    - Finish

A whole slew of tools will now appear in your Administrative Tools folder. The
provided Authorization Manager tool is OK to look at and mess around with, but
it can't be used for our purposes because it doesn't support using arbitrary
users from external datbases; it only allows users defined within an actual
Active Directory instance. Note that AzMan does support this capability, just
that the UI does not provide a way to specify it.

In general, the idea behind AzMan is about separation of concerns. The goal is
to allow developers to write code to a specification while allowing the business
to change its rules about policy without having to touch the code again. AzMan
accomplishes this by defining 3 major concepts: Operations, Tasks, and Roles.
These correspond to 3 main actors of any enterprise application: Developers,
Business Analysts, and System Administrators.

Operations are the lowest-level objects that define which individual functions
need to be performed in an application. Examples include "Create User", "View
Shopping List", "Broadcast Message". Convienently, these operations nicely
correlate to Controller Actions. They also have a ring of CRUD to them (although
some operations fall outside the CRUD model).

Tasks can combine many operations to form one unit of work. These are typically
defined and maintained by Business Analysts. Examples of these might include:
"Manage Users", "Develop Leads", or "Prepare Notification". None of these
definitions need to be known by the application, only within the AzMan policy
store. Although developers can query to see if a user has access to a resource
by checking their ability to perform a task, this is not a recommended practice.

Roles are the highest-level objects that assign a collection of users or groups
to set of tasks. Examples include: "System Administrator", "Basic User", or
"Message Approver". Most role-based access systems are based on only roles. For
many applications, this is sufficient, but when applications grow in size and
complexity, it becomes difficult to maintain, especially across many different
applications. Therefore, it is recommeneded that developers specify access to
resources on operations rather than roles and leave the role assignments to the
responsibilty of System Administrators.

For more information on AzMan, refer to these links:

 - `Developing Applications Using Windows Authorization Manager <http://msdn.microsoft.com/en-us/library/aa480244.aspx>`_
 - `The .NET Developer's Guide to Identity <http://msdn.microsoft.com/en-us/library/aa480245.aspx>`_

Introducing SecurityManager
---------------------------

SecurityManager.Web is an assembly that integrates AzMan with ASP.NET MVC and
ASP.NET Membership. An HttpModule is implemented so that all the details of
tracking the identity of a user (authentication) and obtaining an instance to
the AzMan COM objects are handled upon every request. It provides a set of
wrappers and APIs to allow developers to write code that allows them to check
permissions for a particular Operation in 3 ways:

1. Declaratively thru the use of the ``Operation`` or ``[AzManPermission]`` attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``[Operation]`` attribute is best placed above each publically accessible
Controller action:

.. code-block:: c#

  using System.Web.Mvc;
  using SecurityManager.Web;
  
  namespace HAN.Controllers
  {
      public class ArchiveController : Controller
      {
          [Operation("View Archive")]
          public ActionResult List() {
              return View();
          }
      }
  }

In the example above, we are saying that the ``List`` action of the
ArchiveController is only allowed by users that have been granted access to the
"View Archive" operation. The ``[Operation]`` attribute is implemented using an
ASP.NET MVC action filter. This means that these kinds of attributes can only be
used on Controller actions.

To declare an operation on non-action methods, you can use a CAS (Code-Access
Security) based attribute. CAS attributes are automatically checked by the
runtime before a call is made. This relies on the ``HttpContext.Current``
instance being properly set, so be careful when writing unit tests. An example
of this kind of attribute uses the ``[AzManPermission]``.

.. code-block:: c#

	using SecurityManager.Web;
	using System.Security.Permissions;
	
	namespace SecurityManager
	{
	    public class GlobalApplication : System.Web.HttpApplication
	    {
	        [AzManPermission(SecurityAction.Demand, Operation = "Login")]
	        protected void Session_Start() {
	        }
	    }
	}

The above prevents users that are not allowed to Login to this site from being
able to proceed.

2. Declaratively on server pages using the ``<azman:PermissionControl>``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say you have a navigation menu that you wish to be dynamic, based on which
user is logged in and what operations they have access to. This is easy by using
the ``<azman:PermissionControl>`` server-side control. The PermissionControl has
an Operation attribute that should be pretty self-explanatory. Content within
the PermissionControl tags will be rendered only if the current user has access
to the specified Operation.

.. code-block:: html

	<ul class="nav">
	    <azman:PermissionControl runat="server" operation="View Users">
	        <li><a href='/ViewUsers.aspx'>View Users</a></li>
	    </azman:PermissionControl>
	    <azman:PermissionControl runat="server" operation="View Groups">
	        <li><a href='/ViewGroups.aspx'>View Groups</a></li>
	    </azman:PermissionControl>
	    <azman:PermissionControl runat="server" operation="View Applications">
	        <li><a href='/ViewApps.aspx'>View Applications</a></li>
	    </azman:PermissionControl>
	    <azman:PermissionControl runat="server" operation="View Operations">
	        <li><a href='/ViewOps.aspx'>View Operations</a></li>
	    </azman:PermissionControl>
	    <azman:PermissionControl runat="server" operation="View Tasks">
	        <li><a href='/ViewTasks.aspx'>View Tasks</a></li>
	    </azman:PermissionControl>
	    <azman:PermissionControl runat="server" operation="View Roles">
	        <li><a href='/ViewRoles.aspx'>View Roles</a></li>
	    </azman:PermissionControl>
	</ul>

3. Programatically by using the ``User.CanPerform`` extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every User (``IPrincipal``) attribute gets an extension ``CanPerform(string
operation)`` so that you can programmatically check for permission of an
operation. Here's an example of its usage:

.. code-block:: html

	<asp:content id="indexContent" contentplaceholderid="MainContent" runat="server">
	
	    Your Username: <%= Username %>	
	    <br />
	
	    <% if(User.CanPerform("View Roles")) { %>
	        Assigned Roles: <%= User.Roles %>
	    <% } %>
	
	</asp:Content>

.. _Windows Server 2003 SP1 Administration Tools Pack: http://www.microsoft.com/downloads/details.aspx?familyid=e487f885-f0c7-436a-a392-25793a25bad7&displaylang=en
