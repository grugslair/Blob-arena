using UnityEngine;

public class UiStateManager : MonoBehaviour
{
    public bool simpleLeaderboardModes = true;

    private void Awake()
    {
        UiReferencesStatic.uiStateManager = this;
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.T))
        {
            Debug.Log($"this si the current account {DojoEntitiesStatic.currentAccount.Address.Hex()}");

            Debug.Log($"This is the amount of blobs loaded in all {DojoEntitiesStatic.allBlobertDict.Count}");
            Debug.Log($"This si the users blobert should be not null {DojoEntitiesStatic.userBlobertData.blobertId.Hex()}");

            Debug.Log($"This is the amount of blobs loaded in twoHashesDict {DojoEntitiesStatic.twoHashesDict.Count}");
            Debug.Log($"This is the amount of blobs loaded in twoMovesDict {DojoEntitiesStatic.twoMovesDict.Count}");
            Debug.Log($"This is the amount of blobs loaded in healthsStorage {DojoEntitiesStatic.healthsList.Count}");
            Debug.Log($"This is the amount of blobs loaded in knockoutsList {DojoEntitiesStatic.knockoutsList.Count}");

            if (DojoEntitiesStatic.knockoutCurrentGame != null)
            {
                Debug.Log(DojoEntitiesStatic.knockoutCurrentGame.blobertA.Hex());
                Debug.Log(DojoEntitiesStatic.knockoutCurrentGame.blobertB.Hex());

                Debug.Log(DojoEntitiesStatic.knockoutCurrentGame.playerA.Hex());
                Debug.Log(DojoEntitiesStatic.knockoutCurrentGame.playerB.Hex());
             
                Debug.Log(DojoEntitiesStatic.knockoutCurrentGame.combatId.Hex());
                Debug.Log("knowouct current game not null");
            }
            else
            {
                Debug.Log("knowouct current game null");
            }

            if (DojoEntitiesStatic.healthsCurrentGame != null)
            {
                Debug.Log(DojoEntitiesStatic.healthsCurrentGame.combatId.Hex());
                Debug.Log(DojoEntitiesStatic.healthsCurrentGame.a);
                Debug.Log(DojoEntitiesStatic.healthsCurrentGame.b);
                Debug.Log("healths current game not null");
            }
            else
            {
                Debug.Log("healths current game null");
            }

            if (DojoEntitiesStatic.twoHashesCurrentGame != null)
            {
                Debug.Log(DojoEntitiesStatic.twoHashesCurrentGame.b.Hex());
                Debug.Log(DojoEntitiesStatic.twoHashesCurrentGame.a.Hex());
                Debug.Log(DojoEntitiesStatic.healthsCurrentGame.combatId.Hex());
                Debug.Log("twoHashes current game not null");
            }
            else
            {
                Debug.Log("twoHashes current game null");
            }

            if (DojoEntitiesStatic.twoMovesCurrentGame != null)
            {
                Debug.Log("twoMoves current game not null");
            }
            else
            {

                Debug.Log("twoMoves current game null");
            }

            if (DojoEntitiesStatic.currentRoundId != null)
            {
                Debug.Log(DojoEntitiesStatic.currentRoundId.Hex());
                Debug.Log("round current id not null");
            }
            else
            {
                Debug.Log("round current id  null");
            }
        }

        if (Input.GetKeyDown(KeyCode.O))
        {
            KeyStorageManager.SaveKeyPair(BlobertUtils.Address0sFix(DojoEntitiesStatic.currentAccount.Address.Hex()), DojoEntitiesStatic.currentAccount.Signer.Inner.Hex());
        }

        if (Input.GetKeyDown(KeyCode.P))
        {
            var keys = KeyStorageManager.GetAllKeyPairs();

            Debug.Log("prob a double debug log");
            Debug.Log(keys);
        }
    }
}



