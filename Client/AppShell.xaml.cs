using Client.Views;

namespace Client;

public partial class AppShell : Shell
{
	public AppShell()
	{
		InitializeComponent();

        // routes
        Routing.RegisterRoute("inventory", typeof(ManageInventory));
        Routing.RegisterRoute("listings", typeof(ManageListings));
    }
}
