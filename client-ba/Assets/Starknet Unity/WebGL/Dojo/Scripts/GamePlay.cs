using UnityEngine;
using Types;
using Utils;
using StarkSharp.Rpc.Utils;
using Dojo;

public class GamePlay : MonoBehaviour
{
    private string gameObjectName = "GameObjectName"; // replace with the name of the game object the script is attached to
    //private string dojoConfig.worldAddress = PlayerPrefs.GetString("World Address");
    [SerializeField] private  WorldManagerData dojoConfig;

    //public void Entity(string component, Query query, int offset = 0, int length = 0)
    //{
    //    string[] calldata = new string[]{
    //        StarknetOps.CalculateFunctionSelector(component),
    //        query.AddressDomain,
    //        string.Join(",", query.Keys.Select(k => k.ToString())),
    //        offset.ToString(),
    //        length.ToString()
    //    };
    //    string calldataString = JsonUtility.ToJson(new ArrayWrapper { array = calldata });
    //    JSInteropManager.CallContract(dojoConfig.worldAddress, WorldEntryPoints.Get, calldataString, gameObjectName, "Callback");
    //}

    //public void Entities(string component, int length)
    //{
    //    string[] calldata = new string[]{
    //        component,
    //        StarknetOps.CalculateFunctionSelector(length.ToString())
    //    };
    //    string calldataString = JsonUtility.ToJson(new ArrayWrapper { array = calldata });
    //    JSInteropManager.CallContract(dojoConfig.worldAddress, WorldEntryPoints.Entities, calldataString, gameObjectName, "Callback");
    //}

    public void Component(string name)
    {
        string[] calldata = new string[]{
            StarknetOps.CalculateFunctionSelector(name)
        };
        string calldataString = JsonUtility.ToJson(new ArrayWrapper { array = calldata });
        JSInteropManager.CallContract(dojoConfig.worldAddress, WorldEntryPoints.Component, calldataString, gameObjectName, "Callback");
    }

    public void Execute(string[] callData)
    {
        string calldataString = JsonUtility.ToJson(new ArrayWrapper { array = callData });
        JSInteropManager.SendTransaction(dojoConfig.worldAddress, WorldEntryPoints.Execute, calldataString, gameObjectName, "Callback");
    }

    public void Callback(string response)
    {
        JsonResponse jsonResponse = JsonUtility.FromJson<JsonResponse>(response);
        Debug.Log(jsonResponse.result);
    }
}
