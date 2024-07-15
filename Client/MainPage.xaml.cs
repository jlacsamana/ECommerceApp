namespace Client;

public partial class MainPage : ContentPage
{

	public MainPage()
	{
		InitializeComponent();
	}

    private async void OnSSOLogin(object sender, EventArgs e)
    {
        // add logic to allow SSO login here


        // if succeeded
        await Shell.Current.GoToAsync("//loggedInHomePage");

    }
}

