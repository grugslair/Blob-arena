using DG.Tweening;
using Dojo;
using DojoContractCommunication;
using System;
using System.Collections;
using System.Globalization;
using System.Numerics;
using TMPro;
using UnityEngine;
using UnityEngine.UI;
using Random = UnityEngine.Random;
using Vector3 = UnityEngine.Vector3;

public class LoginScreenBehaviour : Menu
{
    // this is the way

    // firts anim starts
    // on end it calls the anim for the button
    // on end it calls the fade in
    // on end this should also call the interactive on

    // when the burner is done change the text to the the address and start the blobert anim with the button
    // once both are done the interactive on the button is on
    // on groundhit the camera should shake
    // the particle should play

    // bloberts should blob
    //till the new blobert is minted, once minter we go onto the next screen

    [SerializeField] private RawImage shadowImage;
    [SerializeField] private GameObject realBackdrop;
    [SerializeField] private GameObject fakeBackdrop;

    [SerializeField] private RectTransform bloberLeft;
    [SerializeField] private RectTransform bobertRight;

    [SerializeField] private Transform shakingTransform;

    [SerializeField] private TMP_Text addressText;

    [SerializeField] private GameManager gameManager;

    [SerializeField] private Menu mainMenu;
    [SerializeField] private MenuManager menuManager;

    [SerializeField] private WorldManager worldManager;

    [SerializeField] private GameObject popUp;

    private bool burnerCreated = false;
  
    public void CreateBurner()
    {
        Debug.Log("Creating Burner");
        gameManager.CreateBurner();    // put the burenr stuff into a fucn
    }

    private void Update()
    {
        if (!burnerCreated && DojoEntitiesStorage.currentAccount != null)
        {
            burnerCreated = true;

            var animator = transform.GetComponent<Animator>();
            animator.SetTrigger("LoggedIn");

            addressText.text = $"{DojoEntitiesStorage.currentAccount.Address.Hex().Substring(0,6)}...";
            
            //DojoEntitiesStatic.burnerManagerSaver.AddAccountToLocalData(DojoEntitiesStatic.currentAccount.Address.Hex(), DojoEntitiesStatic.currentAccount.Signer.Inner.Hex());

            worldManager.LoadData();    // this is  afucntion to sync on demand easy

            popUp.SetActive(true);
        }

        if (burnerCreated && DojoEntitiesStorage.userBloberts.Count > 0)
        {
            menuManager.OpenMenu(mainMenu);
        }
    }

    public void Shake(float duration)
    {
        StartCoroutine(ShakeCoroutine(duration, 10f));
    }

    public void StartBlobbing()
    {
        realBackdrop.SetActive(true);
        fakeBackdrop.SetActive(false);

        transform.GetComponent<Animator>().enabled = false;
        
        bloberLeft.DOAnchorPosY(bloberLeft.anchoredPosition.y + 30, 0.4f)
           .SetLoops(-1, LoopType.Yoyo) 
           .SetEase(Ease.InOutQuad);

        bobertRight.DOAnchorPosY(bobertRight.anchoredPosition.y + 25, 0.4f)
           .SetLoops(-1, LoopType.Yoyo)
           .SetEase(Ease.InOutQuad)
           .SetDelay(0.5f);
    }

    IEnumerator ShakeCoroutine(float duration, float magnitude)
    {
        Vector3 originalPosition = shakingTransform.localPosition;
        float elapsedTime = 0f;

        while (elapsedTime < duration)
        {
            float x = Random.Range(-1f, 1f) * magnitude;
            float y = Random.Range(-1f, 1f) * magnitude;

            shakingTransform.localPosition = new Vector3(x, y, originalPosition.z);

            elapsedTime += Time.deltaTime;

            // Gradually reduce the magnitude over time
            magnitude = Mathf.Lerp(magnitude, 0, elapsedTime / duration);

            yield return null; // Wait until the next frame
        }

        // Reset the camera position
        shakingTransform.localPosition = originalPosition;
    }

    public async void MintBlobert()
    {
        var endpointData = new EndpointDojoCallStruct
        {
            account = DojoEntitiesStorage.currentAccount,
            addressOfSystem = DojoEntitiesStorage.worldManagerData.blobertContractAddress,
            functionName = BlobertActionsContract.FunctionNames.Mint.EnumToString()
        };

        var structData = new BlobertActionsContract.MintStruct
        {
            owner = DojoEntitiesStorage.currentAccount.Address
        };

        var something = await BlobertActionsContract.MintCall(structData, endpointData);
    }





}
