using Dojo.Starknet;
using System;
using TMPro;
using UnityEngine;

public class CreateLobbyBehavior : Menu
{
    public MenuManager menuManager;
    public Menu battlePhase;
    //se the data for the blobert and have an input field take waya the button

    public BlobertCardData blobertCardData;
    public TMP_InputField inputFieldOtherPlayer;

    public TMP_Text idText;
    public TMP_Text addressText;

    private void OnEnable()
    {
        var blobert = DojoEntitiesStatic.userBlobertData;

        addressText.text = DojoEntitiesStatic.currentAccount.Address.Hex();

        blobertCardData.SetBicepText(blobert.stats.strength.ToString());
        blobertCardData.SetShoesText(blobert.stats.speed.ToString());
        blobertCardData.SetSwordText(blobert.stats.attack.ToString());
        blobertCardData.SetShieldText(blobert.stats.defense.ToString());

        idText.text = $"ID: {BlobertUitls.HexToBigInt(blobert.blobertId.Hex())}";
    }

    private DateTime lastInteractionWithContract = DateTime.MinValue;

    public async void CreateLobby()
    {
        double secondsSinceLastCommit = (DateTime.Now - lastInteractionWithContract).TotalSeconds;

        if (secondsSinceLastCommit < 2)
        {
            Debug.Log("You are creating a lobby too fast");
            return;
        }
        else
        {
            lastInteractionWithContract = DateTime.Now;
        }

        // if input field is empty return
        if (string.IsNullOrEmpty(inputFieldOtherPlayer.text))
        {
            return;
        }

        var endpoint = new DojoCallsStatis.EndpointDojoCallStruct
        {
            account = DojoEntitiesStatic.currentAccount,
            functionName = "new",
            addressOfSystem = DojoCallsStatis.knockoutAddress
        };

        Debug.Log("Creating new game");
        Debug.Log("Player A: " + DojoEntitiesStatic.currentAccount.Address.Hex());
        Debug.Log("Player B: " + new FieldElement(inputFieldOtherPlayer.text).Hex());
        Debug.Log("Blobert A: " + DojoEntitiesStatic.userBlobertData.blobertId.Hex());

        //for loop to check all the blobs and if the other player has the blobert

        var blobertFound = false;
        var blobertId = new FieldElement("0");

        foreach (var blobert in DojoEntitiesStatic.allBlobertDict)
        {
            if (blobert.Value.owner.Hex() == inputFieldOtherPlayer.text)
            {
                blobertId = blobert.Value.blobertId;
                blobertFound = true;
            }
        }

        if (!blobertFound)
        {
            Debug.Log("Blobert not found");
            return;
        }


        var dataStruct = new DojoCallsStatis.CreateNewGameStruct
        {
            player_a = DojoEntitiesStatic.currentAccount.Address,
            player_b = new FieldElement(inputFieldOtherPlayer.text),
            blobert_aID = DojoEntitiesStatic.userBlobertData.blobertId,
            blobert_bID = blobertId,
        };

        var transaction = await DojoCallsStatis.CreateNewGame(dataStruct, endpoint);
    }

    void Update()
    {
        if (DojoEntitiesStatic.healthsCurrentGame != null && DojoEntitiesStatic.knockoutCurrentGame != null)
        {
            Debug.Log("we move to the next phase");
            menuManager.OpenMenu(battlePhase);
        }

        for (int i = DojoEntitiesStatic.knockoutsList.Count - 1; i >= 0; i--)
        {
            var currentKnockout = DojoEntitiesStatic.knockoutsList[i];

            if (DojoEntitiesStatic.knockoutCurrentGame != null && DojoEntitiesStatic.healthsCurrentGame != null)
            {
                break;
            }

            if (BlobertUitls.Address0sFix(currentKnockout.playerA.Hex()) == DojoEntitiesStatic.currentAccount.Address.Hex() || BlobertUitls.Address0sFix(currentKnockout.playerB.Hex()) == DojoEntitiesStatic.currentAccount.Address.Hex())
            {
                // the knowouct round made contains the player
                // find the healths round by doing another loop ffs

                for (int x = 0; x < DojoEntitiesStatic.healthsList.Count; x++)
                {
                    //sanity check

                    var health = DojoEntitiesStatic.healthsList[x];
                    if (currentKnockout.combatId.Hex() == health.combatId.Hex())
                    {
                        // this is the same hex as the knowcout

                        if (health.a > 0 && health.b > 0)
                        {
                            DojoEntitiesStatic.knockoutCurrentGame = currentKnockout;
                            DojoEntitiesStatic.healthsCurrentGame = health;
                            DojoEntitiesStatic.currentRoundId = currentKnockout.combatId;

                            break;
                        }
                        else
                        {
                            continue;
                        }
                    }
                }

            }
            else
            {
                //delete from the list
                DojoEntitiesStatic.knockoutsList.RemoveAt(i);
                continue;
            }

        }


    }
}
