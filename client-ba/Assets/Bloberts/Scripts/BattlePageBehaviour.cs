using Dojo.Starknet;
using System;
using TMPro;
using UnityEngine;

public class BattlePageBehaviour : Menu
{
    [SerializeField] private TMP_Text addressPlayerText;
    [SerializeField] private TMP_Text addressEnemyText;

    [SerializeField] private GameObject commitButton;
    [SerializeField] private GameObject revealButton;
    [SerializeField] private GameObject waitButton;
    [SerializeField] private GameObject winnerBanner;
    [SerializeField] private TMP_Text winnerText;

    [SerializeField] private TMP_Text playerHpText;
    [SerializeField] private TMP_Text enemyHpText;

    [SerializeField] private BlobertCardData playerBlobertCardData;
    [SerializeField] private BlobertCardData enemyBlobertCardData;

    [SerializeField] private int secretNumber;
    [SerializeField] private BlobertUtils.Move lastMove;

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
        if (DojoEntitiesStatic.knockoutCurrentGame.playerA.Hex() == DojoEntitiesStatic.currentAccount.Address.Hex())
        {
            playerLetter = "a";
        }
        else
        {
            playerLetter = "b";
        }

        UpdateData();
        secretNumber = UnityEngine.Random.Range(0, 100000);
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

            winnerBanner.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStatic.knockoutCurrentGame.playerB.Hex().Substring(0, 6)} wins";

            return;
        }

        else if (DojoEntitiesStatic.healthsCurrentGame.b == 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerBanner.SetActive(true);
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

            var pedersanOutput = BlobertUtils.PedersenFunction(secretNumber, action);

            var pedersenHash = new FieldElement(pedersanOutput);

            lastMove = (BlobertUtils.Move)action;

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
        if (playerLetter == "a")
        {
            addressEnemyText.text = DojoEntitiesStatic.knockoutCurrentGame.playerB.Hex().Substring(0, 7);
            addressPlayerText.text = DojoEntitiesStatic.knockoutCurrentGame.playerA.Hex().Substring(0, 7);

            playerBlobertCardData.SetBlobertId(DojoEntitiesStatic.knockoutCurrentGame.blobertA);
            enemyBlobertCardData.SetBlobertId(DojoEntitiesStatic.knockoutCurrentGame.blobertB);

            playerHpText.text = $"HP: {DojoEntitiesStatic.healthsCurrentGame.a}";
            enemyHpText.text = $"HP: {DojoEntitiesStatic.healthsCurrentGame.b}";

        }
        else if (playerLetter == "b")
        {
            addressPlayerText.text = DojoEntitiesStatic.knockoutCurrentGame.playerB.Hex().Substring(0, 7);
            addressEnemyText.text = DojoEntitiesStatic.knockoutCurrentGame.playerA.Hex().Substring(0, 7);

            enemyBlobertCardData.SetBlobertId(DojoEntitiesStatic.knockoutCurrentGame.blobertA);
            playerBlobertCardData.SetBlobertId(DojoEntitiesStatic.knockoutCurrentGame.blobertB);

            enemyHpText.text = $"HP: {DojoEntitiesStatic.healthsCurrentGame.a}";
            playerHpText.text = $"HP: {DojoEntitiesStatic.healthsCurrentGame.b}";
        }
    }
}
