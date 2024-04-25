using System.Runtime.InteropServices;
using UnityEngine;

public class KeyStorageManager : MonoBehaviour
{
    // Import the JavaScript functions from the jslib file

    public static void SaveKeyPair(string publicAddress, string privateKey)
    {

    }

    public static string GetAllKeyPairs()
    {

            return GetAllKeysFromPlayerPrefs();

    }

    private static string GetAllKeysFromPlayerPrefs()
    {
        var keys = "";
        foreach (var key in PlayerPrefs.GetString("keys", "").Split(','))
        {
            if (!string.IsNullOrEmpty(key))
            {
                var value = PlayerPrefs.GetString(key);
                keys += key + ":" + value + ",";
            }
        }

        Debug.Log("these are all the keys");
        Debug.Log(keys);
        return keys.TrimEnd(',');
    }
}
