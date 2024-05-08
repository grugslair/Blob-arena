using DG.Tweening;
using Dojo.Starknet;
using DojoContractCommunication;
using System;
using System.Numerics;
using TMPro;
using UnityEngine;
using Vector2 = UnityEngine.Vector2;

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

    private Tweener _tweenBloberLeft;
    private Tweener _tweenBobertRight;

    public int gameState = 0;
    public string playerLetter = "";

    private DateTime lastInteractionWithContract = DateTime.MinValue;

    private bool _isBloberLeftAnimating = false;
    private bool _isBobertRightAnimating = false;

    private bool _commiting = true;

    private void Start()
    {
       UiReferencesStatic.battlePageBehaviour = this;

        originalPositionBloberLeft = blobertLeft.anchoredPosition;
        originalPositionBobertRight = blobertRight.anchoredPosition;
    }

    private void OnEnable()
    {
        if (DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerA.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex())
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
    }

    public void CallFromDataToUpdate()
    {
        if (CheckPlayerHealths())
        {
            Debug.Log("the game is over one of the two died");
            return;
        }

        if (_commiting)
        {
            if (DojoEntitiesStorage.twoHashesCurrentGame != null)
            {
                var a = DojoEntitiesStorage.twoHashesCurrentGame.dojoA.Hex();
                var b = DojoEntitiesStorage.twoHashesCurrentGame.dojoB.Hex();
                int state = 0;

                if (a == BlobertUtils.emptyFieldElement) state |= 1;
                if (b == BlobertUtils.emptyFieldElement) state |= 2;

                switch (state)
                {
                    case 0:

                        StopBobertRightAnimation();
                        StopBloberLeftAnimation();

                        commitButton.SetActive(false);
                        revealButton.SetActive(true);
                        waitButton.SetActive(false);

                        _commiting = false;

                        break;
                    case 1:
                        // Only a is not empty
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
            if (DojoEntitiesStorage.twoMovesCurrentGame != null)
            {
                var a = DojoEntitiesStorage.twoMovesCurrentGame.dojoA;
                var b = DojoEntitiesStorage.twoMovesCurrentGame.dojoB;
                int state = 0;

                if (a == BlobertUtils.MoveN.NONE) state |= 1;
                if (b == BlobertUtils.MoveN.NONE) state |= 2;

                switch (state)
                {
                    case 0:
                        // Both are empty
                        StopBloberLeftAnimation();
                        StopBobertRightAnimation();

                        _commiting = true;

                        // both are empty therefore we blob
                        break;
                    case 1:
                        // Only a is not empty
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
                        StartBloberLeftAnimation();
                        StartBobertRightAnimation();

                        // but if the hashes are also empty
                        if (DojoEntitiesStorage.twoHashesCurrentGame.dojoA.Hex() == BlobertUtils.emptyFieldElement && DojoEntitiesStorage.twoHashesCurrentGame.dojoB.Hex() == BlobertUtils.emptyFieldElement)
                        {
                            _commiting = true;

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
        if (DojoEntitiesStorage.healthsCurrentGame == null)
        {
            return false;
        }

        UpdateFrontEndData();

        if (DojoEntitiesStorage.healthsCurrentGame.dojoA <= 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerBanner.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerB.Hex().Substring(0, 6)} wins";

            StopBloberLeftAnimation();
            StartBobertRightAnimation();

            return true;
        }
        else if (DojoEntitiesStorage.healthsCurrentGame.dojoB <= 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerBanner.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerA.Hex().Substring(0, 6)} wins";

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

            Debug.Log("Committing a move");

            switch (lastMove)
            {
                case BlobertUtils.Move.Rush:
                    Debug.Log("Rush");
                    break;
                case BlobertUtils.Move.Beat:
                    Debug.Log("Beat");
                    break;
                case BlobertUtils.Move.Counter:
                    Debug.Log("Counter");
                    break;
            }

            Debug.Log("Secret number: " + secretNumber);
            Debug.Log("Hash: " + pedersenHash.Hex());
            Debug.Log("\n\n");

            var endpoint = new EndpointDojoCallStruct
            {
                account = DojoEntitiesStorage.currentAccount,
                addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
                functionName = ChallengeActionsContract.FunctionNames.CommitMove.EnumToString(),
            };

            var structData = new ChallengeActionsContract.CommitMoveStruct(challengeId: DojoEntitiesStorage.selectedChallengeID, hash: pedersenHash);

            var transaction = await ChallengeActionsContract.CommitMoveCall(structData, endpoint);
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

            Debug.Log("revealing a move");

            switch (lastMove)
            {
                case BlobertUtils.Move.Rush:
                    Debug.Log("Rush");
                    break;
                case BlobertUtils.Move.Beat:
                    Debug.Log("Beat");
                    break;
                case BlobertUtils.Move.Counter:
                    Debug.Log("Counter");
                    break;
            }

            Debug.Log("Secret number: " + secretNumber);
            Debug.Log("\n\n");

            var endpoint = new EndpointDojoCallStruct
            {
                account = DojoEntitiesStorage.currentAccount,
                addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
                functionName = ChallengeActionsContract.FunctionNames.RevealMove.EnumToString(),
            };

            var structData = new ChallengeActionsContract.RevealMoveStruct(challengeId: DojoEntitiesStorage.selectedChallengeID, move: lastMove, salt: new FieldElement(secretNumber.ToString("X")));

            var transaction = await ChallengeActionsContract.RevealMoveCall(structData, endpoint);

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
            addressEnemyText.text = DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerB.Hex().Substring(0, 7);
            addressPlayerText.text = DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerA.Hex().Substring(0, 7);

            playerBlobertCardData.SetBlobertData(DojoEntitiesStorage.knockoutCurrentGame.dojoBlobertA);
            enemyBlobertCardData.SetBlobertData(DojoEntitiesStorage.knockoutCurrentGame.dojoBlobertB);

            playerHpText.text = $"HP: {DojoEntitiesStorage.healthsCurrentGame.dojoA}";
            enemyHpText.text = $"HP: {DojoEntitiesStorage.healthsCurrentGame.dojoB}";

        }
        else if (playerLetter == "b")
        {
            addressPlayerText.text = DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerB.Hex().Substring(0, 7);
            addressEnemyText.text = DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerA.Hex().Substring(0, 7);

            enemyBlobertCardData.SetBlobertData(DojoEntitiesStorage.knockoutCurrentGame.dojoBlobertA);
            playerBlobertCardData.SetBlobertData(DojoEntitiesStorage.knockoutCurrentGame.dojoBlobertB);

            enemyHpText.text = $"HP: {DojoEntitiesStorage.healthsCurrentGame.dojoA}";
            playerHpText.text = $"HP: {DojoEntitiesStorage.healthsCurrentGame.dojoB}";
        }
    }

    public void UpdateLastRound(LastRound lastRound)
    {
        Debug.Log("last round data");
        Debug.Log("i am player " + playerLetter);
        Debug.Log("combat id: " + lastRound.dojoCombatId.Hex());
        Debug.Log("health a: " + lastRound.dojoHealthA);
        Debug.Log("health b: " + lastRound.dojoHealthB);
        Debug.Log("move a: " + lastRound.dojoMoveA);
        Debug.Log("move b: " + lastRound.dojoMoveB);
        Debug.Log("damage a: " + lastRound.dojoDamageA);
        Debug.Log("damage b: " + lastRound.dojoDamageB);
        Debug.Log("\n\n");
    }

    #region Animation region
    public void StartBloberLeftAnimation()
    {
        // Check if animation is already running
        if (_isBloberLeftAnimating) return;

        _tweenBloberLeft?.Kill(); // Safely kill any existing tween first
        _tweenBloberLeft = blobertLeft.DOAnchorPosY(originalPositionBloberLeft.y + 30, 0.4f)
            .SetLoops(-1, LoopType.Yoyo)
            .SetEase(Ease.InOutQuad);

        _isBloberLeftAnimating = true; // Set the flag
    }
    public void StopBloberLeftAnimation()
    {
        // Check if animation is already stopped
        if (!_isBloberLeftAnimating) return;

        _tweenBloberLeft?.Kill();
        blobertLeft.DOAnchorPosY(originalPositionBloberLeft.y, 0.4f).SetEase(Ease.OutQuad);
        _isBloberLeftAnimating = false; // Reset the flag
    }
    public void StartBobertRightAnimation()
    {
        // Check if animation is already running
        if (_isBobertRightAnimating) return;

        _tweenBobertRight?.Kill();
        _tweenBobertRight = blobertRight.DOAnchorPosY(originalPositionBobertRight.y + 25, 0.6f)
            .SetLoops(-1, LoopType.Yoyo)
            .SetEase(Ease.InOutQuad);

        _isBobertRightAnimating = true; // Set the flag
    }
    public void StopBobertRightAnimation()
    {
        // Check if animation is already stopped
        if (!_isBobertRightAnimating) return;

        _tweenBobertRight?.Kill();
        blobertRight.DOAnchorPosY(originalPositionBobertRight.y, 0.6f).SetEase(Ease.OutQuad);
        _isBobertRightAnimating = false; // Reset the flag
    }
    #endregion

    public void ReturnToMenuButton()
    {
        ClearDojoFightCache(true);
    }

    private void ClearDojoFightCache(bool loss)
    {
        DojoEntitiesStorage.healthsCurrentGame = null;
        DojoEntitiesStorage.twoHashesCurrentGame = null;
        DojoEntitiesStorage.twoMovesCurrentGame = null;
        DojoEntitiesStorage.lastRoundCurrentGame = null;
        DojoEntitiesStorage.knockoutCurrentGame = null;
        DojoEntitiesStorage.currentCombatId = null;

        DojoEntitiesStorage.challengeInvite = null;
        DojoEntitiesStorage.challengeResponse = null;
        DojoEntitiesStorage.selectedChallengeID = null;

        if (loss)
        {
            DojoEntitiesStorage.userChoosenBlobert = null;
        }
    }
}
