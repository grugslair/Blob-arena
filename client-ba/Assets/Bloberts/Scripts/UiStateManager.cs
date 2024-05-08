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
           //debug.log all the current ent

            if (DojoEntitiesStorage.currentAccount != null)
            {
                Debug.Log("current account is not null");
                Debug.Log(DojoEntitiesStorage.currentAccount.Address.Hex());
            }
            else
            {
                Debug.Log("current account is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.challengeInvite != null)
            {
                Debug.Log("challenge invite is not null");
                Debug.Log(DojoEntitiesStorage.challengeInvite.challengeId.Hex());
            }
            else
            {
                Debug.Log("challenge invite is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.challengeResponse != null)
            {
                Debug.Log("challenge response is not null");
                Debug.Log(DojoEntitiesStorage.challengeResponse.challengeId.Hex());
            }
            else
            {
                Debug.Log("challenge response is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.selectedChallengeID != null)
            {
                Debug.Log("selected challenge id is not null");
                Debug.Log(DojoEntitiesStorage.selectedChallengeID.Hex());
            }
            else
            {
                Debug.Log("selected challenge id is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.currentCombatId != null)
            {
                Debug.Log("current round id is not null");
                Debug.Log(DojoEntitiesStorage.currentCombatId.Hex());
            }
            else
            {
                Debug.Log("current round id is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.knockoutCurrentGame != null)
            {
                Debug.Log("knockout current game is not null");
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.combatId.Hex());
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.blobertA.Hex() + " blob a id");
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.blobertB.Hex() + " blob b id");
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.blobertA.Hex() + " player a id");
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.blobertB.Hex() + " player b id");
            }
            else
            {
                Debug.Log("knockout current game is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.healthsCurrentGame != null)
            {
                Debug.Log("healths current game is not null");
                Debug.Log(DojoEntitiesStorage.healthsCurrentGame.combatId.Hex());
                Debug.Log(DojoEntitiesStorage.healthsCurrentGame.a + " health a");
                Debug.Log(DojoEntitiesStorage.healthsCurrentGame.b + " health b");
            }
            else
            {
                Debug.Log("healths current game is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.lastRoundCurrentGame != null)
            {
                Debug.Log("last round current game is not null");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.combatId.Hex());
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.healthA + " health a");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.healthB + " health b");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.moveA + " move a");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.moveB + " move b");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.damageA + " damage a");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.damageB + " damage b");
            }
            else
            {
                Debug.Log("last round current game is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.twoHashesCurrentGame != null)
            {
                Debug.Log("two hashes current game is not null");
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.combatId.Hex());
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.a + " hash a");
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.b + " hash b");
            }
            else
            {
                Debug.Log("two hashes id is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.twoHashesCurrentGame != null)
            {
                Debug.Log("two hashes current game is not null");
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.combatId.Hex());
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.a + " hash a");
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.b + " hash b");
            }
            else
            {
                Debug.Log("two hashes id is null");
            }
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



