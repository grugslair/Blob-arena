using DG.Tweening;
using Dojo.Starknet;
using DojoContractCommunication;
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

    [SerializeField] private RectTransform blobertLeft;
    [SerializeField] private RectTransform blobertRight;


    private Vector2 originalPositionBloberLeft;
    private Vector2 originalPositionBobertRight;

    private Tweener tweenBloberLeft;
    private Tweener tweenBobertRight;

    public int gameState = 0;
    public string playerLetter = "";

    private DateTime lastInteractionWithContract = DateTime.MinValue;

    private bool isBloberLeftAnimating = false;
    private bool isBobertRightAnimating = false;

    private void Start()
    {
       UiReferencesStatic.battlePageBehaviour = this;

        originalPositionBloberLeft = blobertLeft.anchoredPosition;
        originalPositionBobertRight = blobertRight.anchoredPosition;
    }

    private void OnEnable()
    {
        if (DojoEntitiesStorage.knockoutCurrentGame.playerA.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex())
        {
            playerLetter = "a";
        }
        else
        {
            playerLetter = "b";
        }

        CallFromDataToUpdate();

        UpdateFrontEndData();
        secretNumber = UnityEngine.Random.Range(0, 100000);
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Z))
        {
            StartBloberLeftAnimation();
        }
        if (Input.GetKeyDown(KeyCode.X))
        {
            StopBloberLeftAnimation();
        }

        if (Input.GetKeyDown(KeyCode.M))
        {
            StartBobertRightAnimation();
        }
        if (Input.GetKeyDown(KeyCode.N))
        {
            StopBobertRightAnimation();
        }

        //Debug.Log(gameState);
    }


    private bool commiting = true;


    public void CallFromDataToUpdate()
    {
        if (CheckPlayerHealths())
        {
            Debug.Log("the game is over one of the two died");
            return;
        }

        if (commiting)
        {
            Debug.Log("in the commiting state");

            if (DojoEntitiesStorage.twoHashesCurrentGame != null)
            {
                var a = DojoEntitiesStorage.twoHashesCurrentGame.a.Hex();
                var b = DojoEntitiesStorage.twoHashesCurrentGame.b.Hex();
                int state = 0;

                if (a == BlobertUtils.emptyFieldElement) state |= 1;
                if (b == BlobertUtils.emptyFieldElement) state |= 2;

                switch (state)
                {
                    case 0:

                        Debug.Log("both hashes are filled");

                        StopBobertRightAnimation();
                        StopBloberLeftAnimation();

                        commitButton.SetActive(false);
                        revealButton.SetActive(true);
                        waitButton.SetActive(false);

                        commiting = false;

                        break;
                    case 1:
                        // Only a is not empty
                        Debug.Log("Only player A has an empty hash");

                        if (playerLetter == "a")
                        {
                            // i am the one making the other guy wait
                            StartBloberLeftAnimation();
                            StopBobertRightAnimation();

                            commitButton.SetActive(true);
                            revealButton.SetActive(false);
                            waitButton.SetActive(false);
                        }
                        else if (playerLetter == "b")
                        {
                            // a is making me wait
                            StopBloberLeftAnimation();
                            StartBobertRightAnimation();

                            commitButton.SetActive(false);
                            revealButton.SetActive(false);
                            waitButton.SetActive(true);
                        }

                        break;
                    case 2:
                        // Only b is not empty
                        Debug.Log("only Player b has an empty hash");

                        if (playerLetter == "b")
                        {
                            StartBloberLeftAnimation();
                            StopBobertRightAnimation();

                            commitButton.SetActive(true);
                            revealButton.SetActive(false);
                            waitButton.SetActive(false);
                            // i am the one making the other guy wait
                        }
                        else if (playerLetter == "a")
                        {
                            // a is making me wait
                            StopBloberLeftAnimation();
                            StartBobertRightAnimation();

                            commitButton.SetActive(false);
                            revealButton.SetActive(false);
                            waitButton.SetActive(true);
                        }
                        break;
                    case 3:
                        // Both are not empty
                        Debug.Log("The hashes are both empty");

                        StartBloberLeftAnimation();
                        StartBobertRightAnimation();

                        commitButton.SetActive(true);
                        revealButton.SetActive(false);
                        waitButton.SetActive(false);

                        break;
                }
            }
            else
            {
                commitButton.SetActive(true);
                revealButton.SetActive(false);
                waitButton.SetActive(false);

                StartBloberLeftAnimation();
                StartBobertRightAnimation();
            }
        }
        else
        {
            Debug.Log("in the reveal state");

            if (DojoEntitiesStorage.twoMovesCurrentGame != null)
            {
                var a = DojoEntitiesStorage.twoMovesCurrentGame.a;
                var b = DojoEntitiesStorage.twoMovesCurrentGame.b;
                int state = 0;

                if (a == MoveN.NONE) state |= 1;
                if (b == MoveN.NONE) state |= 2;

                switch (state)
                {
                    case 0:
                        Debug.Log("The moves are both full");

                        // Both are empty
                        StopBloberLeftAnimation();
                        StopBobertRightAnimation();

                        commiting = true;

                        // both are empty therefore we blob
                        break;
                    case 1:
                        // Only a is not empty
                        Debug.Log("only a moves is empty");

                        if (playerLetter == "a")
                        {
                            StartBloberLeftAnimation();
                            StopBobertRightAnimation();

                            commitButton.SetActive(false);
                            revealButton.SetActive(true);
                            waitButton.SetActive(false);

                            // i am the one making the other guy wait
                        }
                        else if (playerLetter == "b")
                        {
                            StopBloberLeftAnimation();
                            StartBobertRightAnimation();

                            commitButton.SetActive(false);
                            revealButton.SetActive(false);
                            waitButton.SetActive(true);
                            // a is making me wait
                        }

                        break;
                    case 2:
                        // Only b is not empty
                        Debug.Log("only b moves is empty");

                        if (playerLetter == "b")
                        {
                            StartBloberLeftAnimation();
                            StopBobertRightAnimation();

                            commitButton.SetActive(false);
                            revealButton.SetActive(true);
                            waitButton.SetActive(false);
                        }
                        else if (playerLetter == "a")
                        {
                            StopBloberLeftAnimation();
                            StartBobertRightAnimation();

                            commitButton.SetActive(false);
                            revealButton.SetActive(false);
                            waitButton.SetActive(true);
                        }
                        break;
                    case 3:

                        Debug.Log("Both of them are empty");

                        StartBloberLeftAnimation();
                        StartBobertRightAnimation();


                        // but if the hashes are also empty

                        if (DojoEntitiesStorage.twoHashesCurrentGame.a.Hex() == BlobertUtils.emptyFieldElement && DojoEntitiesStorage.twoHashesCurrentGame.b.Hex() == BlobertUtils.emptyFieldElement)
                        {
                            commiting = true;

                            StartBloberLeftAnimation();
                            StartBobertRightAnimation();
                        }

                        break;
                }
            }
            else
            {
                commitButton.SetActive(false);
                revealButton.SetActive(true);
                waitButton.SetActive(false);

                StartBloberLeftAnimation();
                StartBobertRightAnimation();
            }
        }
        Debug.Log("\n\n");
    }


    public bool CheckPlayerHealths()
    {
        Debug.Log("this is checking the healths of the player");

        if (DojoEntitiesStorage.lastRoundCurrentGame == null)
        {
            return false;
        }


        if (DojoEntitiesStorage.lastRoundCurrentGame.healthA <= 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerBanner.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStorage.knockoutCurrentGame.playerB.Hex().Substring(0, 6)} wins";

            ClearDojoFightCache(true);

            StopBloberLeftAnimation();
            StartBobertRightAnimation();

            return true;
        }
        else if (DojoEntitiesStorage.lastRoundCurrentGame.healthB <= 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerBanner.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStorage.knockoutCurrentGame.playerA.Hex().Substring(0, 6)} wins";

            ClearDojoFightCache(true);

            StartBloberLeftAnimation();
            StopBobertRightAnimation();

            return true;
        }

        return false;
    }



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

            var endpoint = new EndpointDojoCallStruct
            {
                account = DojoEntitiesStorage.currentAccount,
                addressOfSystem = DojoEntitiesStorage.worldManagerData.knockoutContractAddress,
                functionName = KnockoutContract.FunctionNames.Commit.EnumToString(),
            };

            var structData = new KnockoutContract.CommitMoveStruct
            {
                combat_id = DojoEntitiesStorage.knockoutCurrentGame.combatId,  
                hash = pedersenHash 
            };

            var transaction = await KnockoutContract.CommitMove(structData, endpoint);

        }
        catch (Exception ex)
        {
            Debug.Log($"An error occurred: {ex.Message}");
        }

        UpdateFrontEndData();
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

            var endpoint = new EndpointDojoCallStruct
            {
                account = DojoEntitiesStorage.currentAccount,
                addressOfSystem = DojoEntitiesStorage.worldManagerData.knockoutContractAddress,
                functionName = KnockoutContract.FunctionNames.Reveal.EnumToString(),
            };

            var structData = new KnockoutContract.RevealMoveStruct
            {
                combat_id = DojoEntitiesStorage.knockoutCurrentGame.combatId,
                move = lastMove,
                salt = new FieldElement(secretNumber.ToString("X"))
            };

            var transaction = await KnockoutContract.RevealMove(structData, endpoint);

            UpdateFrontEndData();
        }
        catch
        {
            Debug.Log("everythign is broken");
        }
    }

    public void UpdateFrontEndData()
    {
        if (playerLetter == "a")
        {
            addressEnemyText.text = DojoEntitiesStorage.knockoutCurrentGame.playerB.Hex().Substring(0, 7);
            addressPlayerText.text = DojoEntitiesStorage.knockoutCurrentGame.playerA.Hex().Substring(0, 7);

            playerBlobertCardData.SetBlobertData(DojoEntitiesStorage.knockoutCurrentGame.blobertA);
            enemyBlobertCardData.SetBlobertData(DojoEntitiesStorage.knockoutCurrentGame.blobertB);

            playerHpText.text = $"HP: {DojoEntitiesStorage.healthsCurrentGame.a}";
            enemyHpText.text = $"HP: {DojoEntitiesStorage.healthsCurrentGame.b}";

        }
        else if (playerLetter == "b")
        {
            addressPlayerText.text = DojoEntitiesStorage.knockoutCurrentGame.playerB.Hex().Substring(0, 7);
            addressEnemyText.text = DojoEntitiesStorage.knockoutCurrentGame.playerA.Hex().Substring(0, 7);

            enemyBlobertCardData.SetBlobertData(DojoEntitiesStorage.knockoutCurrentGame.blobertA);
            playerBlobertCardData.SetBlobertData(DojoEntitiesStorage.knockoutCurrentGame.blobertB);

            enemyHpText.text = $"HP: {DojoEntitiesStorage.healthsCurrentGame.a}";
            playerHpText.text = $"HP: {DojoEntitiesStorage.healthsCurrentGame.b}";
        }
    }



    public void StartBloberLeftAnimation()
    {
        // Check if animation is already running
        if (isBloberLeftAnimating) return;

        tweenBloberLeft?.Kill(); // Safely kill any existing tween first
        tweenBloberLeft = blobertLeft.DOAnchorPosY(originalPositionBloberLeft.y + 30, 0.4f)
            .SetLoops(-1, LoopType.Yoyo)
            .SetEase(Ease.InOutQuad);

        isBloberLeftAnimating = true; // Set the flag
    }

    public void StopBloberLeftAnimation()
    {
        // Check if animation is already stopped
        if (!isBloberLeftAnimating) return;

        tweenBloberLeft?.Kill();
        blobertLeft.DOAnchorPosY(originalPositionBloberLeft.y, 0.4f).SetEase(Ease.OutQuad);
        isBloberLeftAnimating = false; // Reset the flag
    }

    public void StartBobertRightAnimation()
    {
        // Check if animation is already running
        if (isBobertRightAnimating) return;

        tweenBobertRight?.Kill();
        tweenBobertRight = blobertRight.DOAnchorPosY(originalPositionBobertRight.y + 25, 0.6f)
            .SetLoops(-1, LoopType.Yoyo)
            .SetEase(Ease.InOutQuad);

        isBobertRightAnimating = true; // Set the flag
    }

    public void StopBobertRightAnimation()
    {
        // Check if animation is already stopped
        if (!isBobertRightAnimating) return;

        tweenBobertRight?.Kill();
        blobertRight.DOAnchorPosY(originalPositionBobertRight.y, 0.6f).SetEase(Ease.OutQuad);
        isBobertRightAnimating = false; // Reset the flag
    }



    private void ClearDojoFightCache(bool loss)
    {
        DojoEntitiesStorage.healthsCurrentGame = null;
        DojoEntitiesStorage.twoHashesCurrentGame = null;
        DojoEntitiesStorage.twoMovesCurrentGame = null;
        DojoEntitiesStorage.lastRoundCurrentGame = null;
        DojoEntitiesStorage.knockoutCurrentGame = null;
        DojoEntitiesStorage.currentCombatId = null;

        if (loss)
        {
            DojoEntitiesStorage.userChoosenBlobert = null;
        }
    }
}
