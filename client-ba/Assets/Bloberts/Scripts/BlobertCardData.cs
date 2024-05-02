using Dojo.Starknet;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class BlobertCardData : MonoBehaviour
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

    public void SetBlobertData(FieldElement id)
    {
        blobertId = id;

        blobert = DojoEntitiesStorage.allBlobertDict[id.Hex()];

        SetBicepText(blobert.dojoStats.strength.ToString());
        SetSwordValue(blobert.dojoStats.attack.ToString());
        SetShieldText(blobert.dojoStats.defense.ToString());
        SetShoesText(blobert.dojoStats.speed.ToString());

        SetBlobertId();
        SetUpTraitPicture();
    }

    public void SetUpTraitPicture()
    {
        Debug.Log("its getting here");

        var armour = Resources.Load<Texture2D>($"Traits/armour/{BlobertUtils.TraitArmourToFileName(blobert.dojoTraits.armour)}");
        var mask = Resources.Load<Texture2D>($"Traits/masks/{BlobertUtils.TraitMaskToFileName(blobert.dojoTraits.mask)}");
        var jewelry = Resources.Load<Texture2D>($"Traits/jewelry/{BlobertUtils.TraitJewelryToFileName(blobert.dojoTraits.jewelry)}");
        var weapon = Resources.Load<Texture2D>($"Traits/weapons/{BlobertUtils.TraitWeaponToFileName(blobert.dojoTraits.weapon)}");

        if (armour != null)
        {
            Debug.Log("getting here 1");
            _blobertPicArmour.sprite = Sprite.Create(armour, new Rect(0, 0, armour.width, armour.height), new Vector2(0.5f, 0.5f));
        }

        if (mask != null)
        {
            Debug.Log("getting here 2");
            _blobertPicMask.sprite = Sprite.Create(mask, new Rect(0, 0, mask.width, mask.height), new Vector2(0.5f, 0.5f));
        }

        if (jewelry != null)
        {
            Debug.Log("getting here 3");
            _blobertPicJewelry.sprite = Sprite.Create(jewelry, new Rect(0, 0, jewelry.width, jewelry.height), new Vector2(0.5f, 0.5f));
        }

        if (weapon != null)
        {
            Debug.Log("getting here 4");
            _blobertPicWeapon.sprite = Sprite.Create(weapon, new Rect(0, 0, weapon.width, weapon.height), new Vector2(0.5f, 0.5f));
        }
    }

    public void SetSwordValue(string text)
    {
        _swordValueText.text = text;
    }

    public void SetBicepText(string text)
    {
        _bicepValueText.text = text;
    }

    public void SetShieldText(string text)
    {
        _shieldValueText.text = text;
    }

    public void SetShoesText(string text)
    {
        _shieldValueText.text = text;
    }

    public void SetBlobertId()
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
}
