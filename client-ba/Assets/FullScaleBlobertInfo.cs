using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class FullScaleBlobertInfo : MonoBehaviour
{
    [Header("Picture Section")]
    [SerializeField] private Image _blobertArmourImg;
    [SerializeField] private Image _blobertMaskImg;
    [SerializeField] private Image _blobertJewelryImg;
    [SerializeField] private Image _blobertWeaponImg;

    [Header("Traits Section")]
    [SerializeField] private TMP_Text _backgroundTraitText;
    [SerializeField] private TMP_Text _armourTraitText;
    [SerializeField] private TMP_Text _maskTraitText;
    [SerializeField] private TMP_Text _jewelryTraitText;
    [SerializeField] private TMP_Text _weaponTraitText;

    [Header("Stats Section")]
    [SerializeField] private TMP_Text _bicepValueText;
    [SerializeField] private TMP_Text _swordValueText;
    [SerializeField] private TMP_Text _shieldValueText;
    [SerializeField] private TMP_Text _shoesValueText;
    [SerializeField] private TMP_Text _idandOwnerText;
    [SerializeField] private TMP_Text _blobertWinStreakText;
    [SerializeField] private Blobert _blobert;

    public void Initialize(Blobert blobert)
    {
        _blobert = blobert;

        SetImageData();
        SetTraitData();
        SetTextData();

        if (UiReferencesStatic.fullScaleBlobertInfo != null)
        {
            Destroy(UiReferencesStatic.fullScaleBlobertInfo.gameObject);
        }

        UiReferencesStatic.fullScaleBlobertInfo = this;
    }

    private void SetImageData()
    {
        var armour = Resources.Load<Texture2D>($"Traits/armour/{BlobertUtils.TraitArmourToFileName(_blobert.dojoTraits.armour)}");
        var mask = Resources.Load<Texture2D>($"Traits/masks/{BlobertUtils.TraitMaskToFileName(_blobert.dojoTraits.mask)}");
        var jewelry = Resources.Load<Texture2D>($"Traits/jewelry/{BlobertUtils.TraitJewelryToFileName(_blobert.dojoTraits.jewelry)}");
        var weapon = Resources.Load<Texture2D>($"Traits/weapons/{BlobertUtils.TraitWeaponToFileName(_blobert.dojoTraits.weapon)}");

        if (armour != null)
        {
            _blobertArmourImg.sprite = Sprite.Create(armour, new Rect(0, 0, armour.width, armour.height), new Vector2(0.5f, 0.5f));
        }

        if (mask != null)
        {
            _blobertMaskImg.sprite = Sprite.Create(mask, new Rect(0, 0, mask.width, mask.height), new Vector2(0.5f, 0.5f));
        }

        if (jewelry != null)
        {
            _blobertJewelryImg.sprite = Sprite.Create(jewelry, new Rect(0, 0, jewelry.width, jewelry.height), new Vector2(0.5f, 0.5f));
        }

        if (weapon != null)
        {
            _blobertWeaponImg.sprite = Sprite.Create(weapon, new Rect(0, 0, weapon.width, weapon.height), new Vector2(0.5f, 0.5f));
        }
    }

    private void SetTraitData()
    {
        _backgroundTraitText.text = _blobert.dojoTraits.background.ToString().Replace('_', ' ').Trim().ToUpper();
        _armourTraitText.text = _blobert.dojoTraits.armour.ToString().Replace('_', ' ').Trim().ToUpper();
        _maskTraitText.text = _blobert.dojoTraits.mask.ToString().Replace('_', ' ').Trim().ToUpper();
        _jewelryTraitText.text = _blobert.dojoTraits.jewelry.ToString().Replace('_', ' ').Trim().ToUpper();
        _weaponTraitText.text = _blobert.dojoTraits.weapon.ToString().Replace('_', ' ').Trim().ToUpper();
    }

    private void SetTextData()
    {
        _swordValueText.text = _blobert.dojoStats.attack.ToString();
        _bicepValueText.text = _blobert.dojoStats.strength.ToString();
        _shieldValueText.text = _blobert.dojoStats.defense.ToString();
        _shoesValueText.text = _blobert.dojoStats.speed.ToString();
        _idandOwnerText.text = $"ID: {BlobertUtils.HexToBigInt(_blobert.dojoId.Hex()) }\nOwner: {_blobert.dojoOwner.Hex().Substring(0,6)}";
        _blobertWinStreakText.text = $"Win Streak: {7}";
    }

    public void ClosePage()
    {
        UiReferencesStatic.fullScaleBlobertInfo = null;
        Destroy(gameObject);
    }
}
