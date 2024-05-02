using Dojo.Starknet;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class BlobertCardData : MonoBehaviour
{
    [SerializeField] RawImage _blobertBackground;
    [SerializeField] RawImage _blobertPic;

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

    public void SetBlobertPic(Texture2D texture)
    {
        _blobertPic.texture = texture;
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
