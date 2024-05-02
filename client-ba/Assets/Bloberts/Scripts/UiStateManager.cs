using UnityEngine;

public class UiStateManager : MonoBehaviour
{
    //public bool simpleLeaderboardModes = true;
    public GameManager gameManager;

    private void Awake()
    {
        DojoEntitiesStorage.worldManagerData = gameManager.dojoConfig;

        UiReferencesStatic.uiStateManager = this;
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.T))
        {
           
        }

        if (Input.GetKeyDown(KeyCode.O))
        {
            KeyStorageManager.SaveKeyPair(BlobertUtils.Address0sFix(DojoEntitiesStorage.currentAccount.Address.Hex()), DojoEntitiesStorage.currentAccount.Signer.Inner.Hex());
        }

        if (Input.GetKeyDown(KeyCode.P))
        {
            var keys = KeyStorageManager.GetAllKeyPairs();

            Debug.Log("prob a double debug log");
            Debug.Log(keys);
        }
    }
}



