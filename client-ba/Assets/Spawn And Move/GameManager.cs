using System.Collections.Generic;
using System.Threading.Tasks;
using Dojo;
using Dojo.Starknet;
using UnityEngine;
using Random = UnityEngine.Random;

public class GameManager : MonoBehaviour
{
    [SerializeField] WorldManager worldManager;
    [SerializeField] ChatManager chatManager;

    public WorldManagerData dojoConfig;
    //[SerializeField] GameManagerData gameManagerData; 

    public BurnerManager burnerManager;
    private Dictionary<FieldElement, string> spawnedAccounts = new();

    public JsonRpcClient provider;
    public Account masterAccount;

    void Start()
    {
        provider = new JsonRpcClient(dojoConfig.rpcUrl);
        masterAccount = new Account(provider, new SigningKey(dojoConfig.masterPrivateKey), new FieldElement(dojoConfig.masterAddress));

        burnerManager = new BurnerManager(provider, masterAccount);

        worldManager.synchronizationMaster.OnEntitySpawned.AddListener(InitEntity);
        foreach (var entity in worldManager.Entities())
        {
            InitEntity(entity);
        }
    }
    
    public async void CreateBurner()
    {
        var burner = await burnerManager.DeployBurner(new SigningKey());
        spawnedAccounts[burner.Address] = null;
        DojoEntitiesStorage.currentAccount = burner;
    }

    private void InitEntity(GameObject entity)
    {
        foreach (var account in spawnedAccounts)
        {
            if (account.Value == null)
            {
                spawnedAccounts[account.Key] = entity.name;
                break;
            }
        }
    }
}