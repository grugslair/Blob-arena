using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Unity.VisualScripting;
using UnityEngine;

public class MenuManager : MonoBehaviour
{
    [SerializeField] Menu[] _menus;
    [SerializeField] Menu[] _nonReturnableMenus;

    public Menu previousMenu;
    public Menu currentlyOpened;

    public int gamePhase = 1; 
 
    public void OpenMenu(Menu menu)
    {
        if (menu == null)
        {
            Debug.LogError("Menu is null");
            return;
        }

        if (currentlyOpened == menu)  // if the currently opened menu is the same as the one being called to open again this means its actually a close call
        {
            if (previousMenu != null)
            {
                previousMenu.Open();
                currentlyOpened = previousMenu;
            }
            else
            {
                currentlyOpened = null;
            }

            menu.Close();
            
        }
        else
        {
            if (currentlyOpened != null)  // if there is something opened currenlty
            {
               
                currentlyOpened.Close(); //close the one open now

                if (!_nonReturnableMenus.Contains(currentlyOpened))  //chekc if the one that we want to open is in the non savable
                {
                    previousMenu = currentlyOpened; // if it is not we should save it 
                }
                currentlyOpened = menu;
                currentlyOpened.Open();
            }
            else
            {
                menu.Open();
                currentlyOpened = menu;
            }
        }
    }

    private void Update()
    {
      
    }

    public void CloseGame()
    {
        Application.Quit();
    }
}
