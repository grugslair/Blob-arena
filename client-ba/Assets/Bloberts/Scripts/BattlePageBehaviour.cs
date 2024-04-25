using Dojo.Starknet;
using System;
using TMPro;
using UnityEngine;

public class BattlePageBehaviour : Menu
{
    public TMP_Text addressTextA;
    public TMP_Text addressTextB;

    public GameObject commitButton;
    public GameObject revealButton;
    public GameObject waitButton;

    public GameObject winnerThing;
    public TMP_Text winnerText; 

    public TMP_Text hpTextA;
    public TMP_Text hpTextB;

    public BlobertCardData blobertCardDataA;
    public BlobertCardData blobertCardDataB;

    public int secretNumber;
    public BlobertUitls.Move lastMove;

    //public int gameState = 0;

    //0 waiating for self to commit
    //1 waiting for other to commit
    //2 has not revealed self
    // 3 needs to wait for other to reveal

    //states dont work as well

    public int gameState = 0;

    public string playerLetter = "";

    private void Start()
    {
       UiReferencesStatic.battlePageBehaviour = this;
    }

    private void OnEnable()
    {
        UpdateData();
        secretNumber = UnityEngine.Random.Range(0, 100000);

        if (DojoEntitiesStatic.knockoutCurrentGame.playerA.Hex() == DojoEntitiesStatic.currentAccount.Address.Hex())
        {
            playerLetter = "a";
        }
        else
        {
            playerLetter = "b";
        }
    }

    private void Update()
    {
        var zeroHash = new FieldElement("0");

        if (Input.GetKeyDown(KeyCode.Alpha0))
        {
            gameState = 0;
        }
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            gameState = 1;
        }
        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            gameState = 2;
        }
        if (Input.GetKeyDown(KeyCode.Alpha3))
        {
            gameState = 3;
        }

        if (DojoEntitiesStatic.healthsCurrentGame.a == 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerThing.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStatic.knockoutCurrentGame.playerB.Hex().Substring(0, 6)} wins";

            return;
        }

        else if (DojoEntitiesStatic.healthsCurrentGame.b == 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerThing.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStatic.knockoutCurrentGame.playerA.Hex().Substring(0, 6)} wins";

            return;
        }
        

        if (gameState == 0)
        {
            // const check if the user two hashes is done 

            if (playerLetter == "a")
            {
                if (DojoEntitiesStatic.twoHashesCurrentGame.b.Hex() != "0x0000000000000000000000000000000000000000000000000000000000000000")
                {
                    // we wait for other player to commit
                    Debug.Log("this is one the call to change on the A side");
                    gameState = 1;
                }
                else
                {
                    // still need to submit
                    commitButton.SetActive(true);
                    revealButton.SetActive(false);
                    waitButton.SetActive(false);
                }
            }
            else if (playerLetter == "b")
            {
                if (DojoEntitiesStatic.twoHashesCurrentGame.a.Hex() != "0x0000000000000000000000000000000000000000000000000000000000000000")
                {
                    // we wait for other player to commit
                    Debug.Log("this is one the call to change on the B side");
                    gameState = 1;
                }
                else
                {
                    // still need to submit
                    commitButton.SetActive(true);
                    revealButton.SetActive(false);
                    waitButton.SetActive(false);
                }
            }
        }
        else if (gameState == 1)
        {
            commitButton.SetActive(false);
            revealButton.SetActive(false);
            waitButton.SetActive(true);

            if (playerLetter == "b")
            {
                if (DojoEntitiesStatic.twoHashesCurrentGame.b.Hex() != "0x0000000000000000000000000000000000000000000000000000000000000000")
                {
                    gameState = 2;
                }
            }
            else if (playerLetter == "a")
            {
                if (DojoEntitiesStatic.twoHashesCurrentGame.a.Hex() != "0x0000000000000000000000000000000000000000000000000000000000000000")
                {
                    gameState = 2;
                }
            }
        }
        else if (gameState == 2)
        {
            commitButton.SetActive(false);
            revealButton.SetActive(true);
            waitButton.SetActive(false);

            if (DojoEntitiesStatic.twoMovesCurrentGame != null)
            {
                if (playerLetter == "b")
                {
                    if (DojoEntitiesStatic.twoMovesCurrentGame.a != MoveN.NONE)
                    {
                        gameState = 3;
                    }
                }
                else if (playerLetter == "a")
                {
                    if (DojoEntitiesStatic.twoMovesCurrentGame.b != MoveN.NONE)
                    {
                        gameState = 3;
                    }
                }
            }

            if (DojoEntitiesStatic.twoHashesCurrentGame.a.Hex() == "0x0000000000000000000000000000000000000000000000000000000000000000" && DojoEntitiesStatic.twoHashesCurrentGame.b.Hex() == "0x0000000000000000000000000000000000000000000000000000000000000000")
            {
                gameState = 0;
            }
        }
        else if (gameState == 3)
        {
            commitButton.SetActive(false);
            revealButton.SetActive(false);
            waitButton.SetActive(true);

            if (DojoEntitiesStatic.twoMovesCurrentGame.a == MoveN.NONE && DojoEntitiesStatic.twoMovesCurrentGame.b == MoveN.NONE)
            {
                gameState = 0;
            }

            if (DojoEntitiesStatic.twoHashesCurrentGame.a.Hex() == "0x0000000000000000000000000000000000000000000000000000000000000000" || DojoEntitiesStatic.twoHashesCurrentGame.b.Hex() == "0x0000000000000000000000000000000000000000000000000000000000000000")
            {
                gameState = 0;
            }
        }
    }


    private DateTime lastInteractionWithContract = DateTime.MinValue;  


    public async void CallToCommit(int action)
    {
        try
        {
            double secondsSinceLastCommit = (DateTime.Now - lastInteractionWithContract).TotalSeconds;

            if (secondsSinceLastCommit < 1)
            {
                Debug.LogError("You are committing too fast");
                return;
            }
            else {
                lastInteractionWithContract = DateTime.Now; 
            }

            var pedersanOutput = BlobertUitls.PedersenFunction(secretNumber, action);

            var pedersenHash = new FieldElement(pedersanOutput);

            lastMove = (BlobertUitls.Move)action;

            var endpoint = new DojoCallsStatis.EndpointDojoCallStruct
            {
                account = DojoEntitiesStatic.currentAccount,
                addressOfSystem = DojoCallsStatis.knockoutAddress,
                functionName = "commit",
            };

            var structData = new DojoCallsStatis.CommitMoveStruct
            {
                combat_id = DojoEntitiesStatic.knockoutCurrentGame.combatId,  
                hash = pedersenHash 
            };

            var transaction = await DojoCallsStatis.CreateCommitTransaction(structData, endpoint);

        }
        catch (Exception ex)
        {
            Debug.Log($"An error occurred: {ex.Message}");
        }

        UpdateData();
    }

    public async void CallToReveal()
    {
        try
        {
            double secondsSinceLastCommit = (DateTime.Now - lastInteractionWithContract).TotalSeconds;

            if (secondsSinceLastCommit < 1)
            {
                Debug.LogError("You are revealing too fast");
                return;
            }
            else
            {
                lastInteractionWithContract = DateTime.Now;
            }

            var endpoint = new DojoCallsStatis.EndpointDojoCallStruct
            {
                account = DojoEntitiesStatic.currentAccount,
                addressOfSystem = DojoCallsStatis.knockoutAddress,
                functionName = "reveal",
            };

            var structData = new DojoCallsStatis.RevealMoveStruct
            {
                combat_id = DojoEntitiesStatic.knockoutCurrentGame.combatId,
                move = lastMove,
                salt = new FieldElement(secretNumber.ToString("X"))
            };

            var transaction = await DojoCallsStatis.CreateRevealTransaction(structData, endpoint);

            UpdateData();
        }
        catch
        {
            Debug.Log("everythign is broken");
        }
    }

    public void UpdateData()
    {
        addressTextA.text = DojoEntitiesStatic.knockoutCurrentGame.playerA.Hex().Substring(0, 7);
        addressTextB.text = DojoEntitiesStatic.knockoutCurrentGame.playerB.Hex().Substring(0, 7);

        blobertCardDataA.SetBlobertId(DojoEntitiesStatic.knockoutCurrentGame.blobertA);
        blobertCardDataB.SetBlobertId(DojoEntitiesStatic.knockoutCurrentGame.blobertB);

        hpTextA.text = $"HP: {DojoEntitiesStatic.healthsCurrentGame.a}";
        hpTextB.text = $"HP: {DojoEntitiesStatic.healthsCurrentGame.b}";
    }
}
