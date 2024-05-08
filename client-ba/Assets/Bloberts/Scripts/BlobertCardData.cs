using Dojo.Starknet;
using TMPro;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

public class BlobertCardData : MonoBehaviour, IPointerClickHandler
{
    [SerializeField] RawImage _blobertBackground;

    [SerializeField] Image _blobertPicArmour;
    [SerializeField] Image _blobertPicMask;
    [SerializeField] Image _blobertPicJewelry;
    [SerializeField] Image _blobertPicWeapon;

    [SerializeField] TMP_Text _swordValueText;
    [SerializeField] TMP_Text _bicepValueText;
    [SerializeField] TMP_Text _shieldValueText;
    [SerializeField] TMP_Text _shoesValueText;

    [SerializeField] TMP_Text _idValueText;

    public FieldElement blobertId;
    public Blobert blobert;

    [SerializeField] private GameObject _blobertCardFullData;

    public bool loadPicture = true;
    public bool loadText = true;

    public void SetBlobertData(FieldElement id)
    {
        blobertId = id;

        blobert = DojoEntitiesStorage.allBlobertDict[id.Hex()];
        
        SetBlobertId();
        if (loadText)
            SetBlobertText(blobert);

        if (loadPicture)
            SetUpTraitPicture();
    }

    private void SetUpTraitPicture()
    {
        var armour = Resources.Load<Texture2D>($"Traits/armour/{BlobertUtils.TraitArmourToFileName(blobert.dojoTraits.armour)}");
        var mask = Resources.Load<Texture2D>($"Traits/masks/{BlobertUtils.TraitMaskToFileName(blobert.dojoTraits.mask)}");
        var jewelry = Resources.Load<Texture2D>($"Traits/jewelry/{BlobertUtils.TraitJewelryToFileName(blobert.dojoTraits.jewelry)}");
        var weapon = Resources.Load<Texture2D>($"Traits/weapons/{BlobertUtils.TraitWeaponToFileName(blobert.dojoTraits.weapon)}");

        if (armour != null)
        {
            _blobertPicArmour.sprite = Sprite.Create(armour, new Rect(0, 0, armour.width, armour.height), new Vector2(0.5f, 0.5f));
        }

        if (mask != null)
        {
            _blobertPicMask.sprite = Sprite.Create(mask, new Rect(0, 0, mask.width, mask.height), new Vector2(0.5f, 0.5f));
        }

        if (jewelry != null)
        {
            _blobertPicJewelry.sprite = Sprite.Create(jewelry, new Rect(0, 0, jewelry.width, jewelry.height), new Vector2(0.5f, 0.5f));
        }

        if (weapon != null)
        {
            _blobertPicWeapon.sprite = Sprite.Create(weapon, new Rect(0, 0, weapon.width, weapon.height), new Vector2(0.5f, 0.5f));
        }
    }

    private void SetBlobertText(Blobert blobert)
    {
        _bicepValueText.text =  blobert.dojoStats.strength.ToString();
        _swordValueText.text = blobert.dojoStats.attack.ToString();
        _shieldValueText.text = blobert.dojoStats.defense.ToString();
        _shoesValueText.text = blobert.dojoStats.speed.ToString();
    }

    private void SetBlobertId()
    {
        if (_idValueText != null)
        {
            _idValueText.text = $"ID: {BlobertUtils.HexToBigInt(blobert.dojoBlobertId.Hex())}";
        }
    }

    public void SetBlobertBackground(Color color)
    {
        _blobertBackground.color = color;
    }

    public void OnPointerClick(PointerEventData eventData)
    {

        var canvas = GameObject.Find("Canvas"); // this is a no no

        var blobertCardFullData = Instantiate(_blobertCardFullData, canvas.transform);
        blobertCardFullData.GetComponent<FullScaleBlobertInfo>().Initialize(blobert);
    }
}
