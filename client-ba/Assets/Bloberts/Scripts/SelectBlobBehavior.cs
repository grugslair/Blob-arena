using UnityEngine;
using UnityEngine.UI;

public class SelectBlobBehavior : Menu
{
    [SerializeField] private GameObject[] _blobertCardData = new GameObject[3];

    [SerializeField] private GameObject _leftArrow;
    [SerializeField] private GameObject _rightArrow;

    private int _pointer = 1;

    private void OnEnable()
    {
        _pointer = 1;
        PopulateBlobertCards(_pointer);
    }

    public void MovePointer(int direction)
    {
        switch (direction)
        {
            case 1 :
                if (direction + _pointer >= DojoEntitiesStorage.userBloberts.Count - 1)
                {
                    return;
                }

                _pointer++;
                break;

            case -1:

                if (_pointer + direction < 1)
                {
                    return;
                }

                _pointer--;
                break;

            default:
                break;
        }

        PopulateBlobertCards(_pointer);
    }

    private void PopulateBlobertCards(int listIndex)
    {
        for (int i = -1; i < _blobertCardData.Length - 1; i++)
        {
            int adjustedIndex = listIndex - i;

            if (adjustedIndex >= 0 && adjustedIndex < DojoEntitiesStorage.userBloberts.Count && DojoEntitiesStorage.userBloberts[adjustedIndex] != null)
            {
                _blobertCardData[i + 1].SetActive(true);
                var blobertCardComp = _blobertCardData[i + 1].GetComponent<BlobertCardData>();
                blobertCardComp.SetBlobertData(DojoEntitiesStorage.userBloberts[adjustedIndex].dojoBlobertId);

                if (DojoEntitiesStorage.userChoosenBlobert.dojoBlobertId.Hex() == DojoEntitiesStorage.userBloberts[adjustedIndex].dojoBlobertId.Hex())
                {
                    blobertCardComp.SetBlobertBackground(new Color(0.1965083f, 0.5058824f, 0.01960785f, 1));
                }
                else
                {
                    blobertCardComp.SetBlobertBackground(new Color(0.5058824f, 0.05490196f, 0.01960784f, 1));
                }
            }
            else
            {
                _blobertCardData[i + 1].SetActive(false);
            }
        }
    }

    public void SelectThisBlob(int cardClicked)
    {
        DojoEntitiesStorage.userChoosenBlobert = DojoEntitiesStorage.userBloberts[cardClicked];
        PopulateBlobertCards(_pointer);
    }
}
