using Dojo.Starknet;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using UnityEngine;

public class BurnerManagerSaver : MonoBehaviour
{
    private const string PlayerPrefsKey = "BurnerManager";
    [SerializeField] GameManager gameManager;

    public List<Account> accounts = new List<Account>();


    [DllImport("__Internal")]
    private static extern string SaveToLocalStorage(string addressPtr, string keyPtr);

    [DllImport("__Internal")]
    private static extern string getAllData();

    [DllImport("__Internal")]
    private static extern string ClearAllLocalData();


    [System.Serializable]
    public class ArrayOfStringData
    {
        public string[] items;
    }

    void Start()
    {
        DojoEntitiesStatic.burnerManagerSaver = this;
    }

    public void AddAccountToLocalData(string address, string pk)
    {
#if UNITY_WEBGL && !UNITY_EDITOR
          SaveToLocalStorage(address, pk);
#else
        string newString = address + "-" + pk;

        ArrayOfStringData data = LoadDataPlayerPrefs();

        Debug.Log("this is the data " + newString);

        List<string> items = new List<string>();

        try
        {
            items = new List<string>(data.items);
        }
        catch (Exception e)
        {
            Debug.Log(e);

            data = new ArrayOfStringData();

            Debug.Log("this was empty so i made a new one");
        }

        items.Add(newString);

        data.items = items.ToArray();

        string json = JsonUtility.ToJson(data);
        SaveDataPlayerPrefs(json);
#endif

    }

    private ArrayOfStringData LoadDataPlayerPrefs()
    {
        string json = PlayerPrefs.GetString(PlayerPrefsKey, "[]");

        Debug.Log("this is the json " + json);


        try {

            return JsonUtility.FromJson<ArrayOfStringData>(json);
        }
        catch (Exception e)
        {
            Debug.Log(e);
            return new ArrayOfStringData();
        }
    }

    private void SaveDataPlayerPrefs(string data)
    {
        Debug.Log(data);
        PlayerPrefs.SetString(PlayerPrefsKey, data);
        PlayerPrefs.Save();
    }

    public void PrintAllData()
    {
#if UNITY_WEBGL && !UNITY_EDITOR
         getAllData();
#else
        accounts.Clear();

        var data = LoadDataPlayerPrefs();
        Debug.Log("i am pritnign all the data");

        foreach (var item in data.items)
        {

            string[] parts = item.Split('-');
            Debug.Log("Address: " + parts[0]);
            Debug.Log("Private Key: " + parts[1]);

            accounts.Add(new Account(gameManager.provider, new SigningKey(parts[1]), new FieldElement(parts[0])));

            gameManager.burnerManager.Burners.Add(new Account(gameManager.provider, new SigningKey(parts[1]), new FieldElement(parts[0])));
        }
#endif
    }

    public void ClearPlayerPrefs()
    {
#if UNITY_WEBGL && !UNITY_EDITOR
         ClearAllLocalData();
#else
        PlayerPrefs.DeleteKey(PlayerPrefsKey);
        PlayerPrefs.Save();  
        Debug.Log("PlayerPrefs for key '" + PlayerPrefsKey + "' have been cleared.");
#endif
    }

    public void ReturnFromTheJsEnd(string AccountData)
    {
        Debug.Log("this is the data from the js end");
        Debug.Log(AccountData);
    }
}
