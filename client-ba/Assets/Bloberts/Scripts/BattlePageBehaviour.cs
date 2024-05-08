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
                var a = DojoEntitiesStorage.twoHashesCurrentGame.a.Hex();
                var b = DojoEntitiesStorage.twoHashesCurrentGame.b.Hex();
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
                var a = DojoEntitiesStorage.twoMovesCurrentGame.a;
                var b = DojoEntitiesStorage.twoMovesCurrentGame.b;
                int state = 0;

                if (a == MoveN.NONE) state |= 1;
                if (b == MoveN.NONE) state |= 2;

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
                        if (DojoEntitiesStorage.twoHashesCurrentGame.a.Hex() == BlobertUtils.emptyFieldElement && DojoEntitiesStorage.twoHashesCurrentGame.b.Hex() == BlobertUtils.emptyFieldElement)
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

        if (DojoEntitiesStorage.healthsCurrentGame.a <= 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerBanner.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStorage.knockoutCurrentGame.playerB.Hex().Substring(0, 6)} wins";

            StopBloberLeftAnimation();
            StartBobertRightAnimation();

            return true;
        }
        else if (DojoEntitiesStorage.healthsCurrentGame.b <= 0)
        {
            revealButton.SetActive(false);
            commitButton.SetActive(false);
            waitButton.SetActive(false);

            winnerBanner.SetActive(true);
            winnerText.text = $"Player {DojoEntitiesStorage.knockoutCurrentGame.playerA.Hex().Substring(0, 6)} wins";

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
                addressOfSystem = DojoEntitiesStorage.worldManagerData.knockoutContractAddress,
                functionName = ChallengeActionsContract.FunctionNames.CommitMove.EnumToString(),
            };

            var structData = new ChallengeActionsContract.CommitMoveStruct(challengeId: DojoEntitiesStorage.knockoutCurrentGame.combatId, hash: pedersenHash);

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
                addressOfSystem = DojoEntitiesStorage.worldManagerData.knockoutContractAddress,
                functionName = ChallengeActionsContract.FunctionNames.RevealMove.EnumToString(),
            };

            var structData = new ChallengeActionsContract.RevealMoveStruct(challengeId: DojoEntitiesStorage.knockoutCurrentGame.combatId, move: lastMove, salt: new FieldElement(secretNumber));

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

    public void UpdateLastRound(LastRound lastRound)
    {
        Debug.Log("last round data");
        Debug.Log("i am player " + playerLetter);
        Debug.Log("combat id: " + lastRound.combatId.Hex());
        Debug.Log("health a: " + lastRound.healthA);
        Debug.Log("health b: " + lastRound.healthB);
        Debug.Log("move a: " + lastRound.moveA);
        Debug.Log("move b: " + lastRound.moveB);
        Debug.Log("damage a: " + lastRound.damageA);
        Debug.Log("damage b: " + lastRound.damageB);
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
