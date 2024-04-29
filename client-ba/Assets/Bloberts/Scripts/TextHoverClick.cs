using TMPro;
using UnityEngine;
using UnityEngine.EventSystems;

public class TextHoverClick : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
{
    private TMP_Text textComponent;
    private string originalText;

    void Start()
    {
        textComponent = GetComponent<TMP_Text>();
        if (textComponent != null)
        {
            originalText = textComponent.text; 
        }
    }

    public void OnPointerEnter(PointerEventData eventData)
    {
        if (textComponent != null)
        {
            textComponent.text = $"<{originalText}>"; 
        }
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        if (textComponent != null)
        {
            textComponent.text = originalText;
        }
    }

    private void OnDisable()
    {
        if (textComponent != null)
        {
            textComponent.text = originalText; 
        }
    }

    private void OnEnable()
    {
        if (textComponent != null)
        {
            textComponent.text = originalText; 
        }
    }
}
