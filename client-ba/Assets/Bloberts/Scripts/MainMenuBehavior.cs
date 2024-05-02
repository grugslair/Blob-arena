using UnityEngine;

public class MainMenuBehavior : Menu
{
    [SerializeField] private GameObject _joinLobbyButton;
    [SerializeField] private GameObject _createLobbyButton;

    // Start is called before the first frame update
    private void OnEnable()
    {
        // this should set the first blobert in the list as the user choosen blobert

        // the user should not be able to look into a create a lobby or join a lobby if they dont have a blobert
        if (DojoEntitiesStorage.userChoosenBlobert == null)
        {
            // does the user have any bloberts 
            if (DojoEntitiesStorage.userBloberts.Count > 0)
            {
                DojoEntitiesStorage.userChoosenBlobert = DojoEntitiesStorage.userBloberts[0];  
                //set the first by default
                //here local storage just like the burenr can be used to always get the same blob, but rememebr to not save the index but the u128 id
                SetButtonsState(true);
            }
            else
            {
                SetButtonsState(false);
            }
        }

        CheckForALiveLobby();
    }

    private void SetButtonsState(bool hasBlob)
    {
        if (hasBlob)
        {
            _joinLobbyButton.GetComponent<UnityEngine.UI.Button>().interactable = true;
            _joinLobbyButton.GetComponent<CanvasGroup>().alpha = 1f;
            _joinLobbyButton.GetComponent<CanvasGroup>().interactable = true;

            _createLobbyButton.GetComponent<UnityEngine.UI.Button>().interactable = true;
            _createLobbyButton.GetComponent<CanvasGroup>().alpha = 1f;
            _createLobbyButton.GetComponent<CanvasGroup>().interactable = true;
        }
        else
        {
            _joinLobbyButton.GetComponent<UnityEngine.UI.Button>().interactable = false;
            _joinLobbyButton.GetComponent<CanvasGroup>().alpha = 0.5f;
            _joinLobbyButton.GetComponent<CanvasGroup>().interactable = false;

            _createLobbyButton.GetComponent<UnityEngine.UI.Button>().interactable = false;
            _createLobbyButton.GetComponent<CanvasGroup>().alpha = 0.5f;
            _createLobbyButton.GetComponent<CanvasGroup>().interactable = false;
        }
    }

    private void CheckForALiveLobby()
    {
        // check if there is a lobby that is still open
        // if there is one, join it
        // if there is none, create one
    }

    void Update()
    {
        
    }
}
