using Dojo.Starknet;
using dojo_bindings;
using System;
using System.Threading.Tasks;
using UnityEngine;

public static class DojoCallsStatis
{
  
    //Local
    //public static readonly string knockoutAddress = "0x66821c7071e66a727918207afb0255e5dac1677b1732a95104c7672fc98d51e";
    //public static readonly string blobertActionsAddress = "0x3e2408ea9affd43d731fcb31e67f7c2c6899cef4c1279dc597dc5d14b240d12";

    //public static readonly string worldAddress = "0x3a0394af68d1727a0019949a94fa584e8bc132903d49bb545888eb1bd427cf4";

    //public static readonly string masterAddress = "0xb3ff441a68610b30fd5e2abbf3a1548eb6ba6f3559f2862bf2dc757e5828ca";
    //public static readonly string masterPrivateKey = "0x2bbf4f9fd0bbb2e60b0316c1fe0b76cf7a4d0198bd493ced9b8df2a3a24d68a";

    //slot
    public static readonly string knockoutAddress = "0x5ca704bee322163577a552e6debdbe6c7b20e209cbeae8e5fbada33ea6510ee";
    public static readonly string blobertActionsAddress = "0x212384234554c179f0875ffc07db99a4952532f61c76cb43d6ea14d0491b610";

    public static readonly string worldAddress = "0x786c41c25759a24772df96df1272cded0b118b64df75c77fa9d5aa669c25b66";

    public static readonly string masterAddress = "0x472c5f0ee5e5224a198e4cd4e26fd7cef51acd64778e0a2fca5af1697d5e5e";
    public static readonly string masterPrivateKey = "0xb320c4fe6c2a03aa2b915f9b3e92654c257dec19c1bf77fefa004690bd65eb";

    #region structs structure for calls

    public struct EndpointDojoCallStruct
    {
        public Account account;
        public string functionName;
        public string addressOfSystem;
    }

    public struct MintBlobertStruct
    {
        public FieldElement owner;
    }

    public struct CreateNewGameStruct
    {
        public FieldElement player_a;
        public FieldElement player_b;

        public FieldElement blobert_aID;
        public FieldElement blobert_bID;
    }

    public struct CommitMoveStruct
    {
        public FieldElement combat_id;
        public FieldElement hash;
    }

    public struct RevealMoveStruct
    {
        public FieldElement combat_id;
        public BlobertUtils.Move move;
        public FieldElement salt;
    }

    public struct VerifyMoveStruct
    {
        public FieldElement combat_id;
    }

    #endregion

    #region dojo calls

    public static async Task<FieldElement> MintBlobert(MintBlobertStruct dataStruct, EndpointDojoCallStruct endpointData)
    {
        try
        {
            var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
            {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                       dataStruct.owner.Inner
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
            });

            return transaction;
        }
        catch (Exception ex)
        {
            Debug.Log("issue with mint" + ex.Message);
            return null;
        }
    }

    public static async Task<FieldElement> CreateNewGame(CreateNewGameStruct dataStruct, EndpointDojoCallStruct endpointData)
    {

        Debug.Log("CreateNewGameStruct " + dataStruct.player_a.Hex());
        Debug.Log("CreateNewGameStruct " + dataStruct.player_b.Hex());
        Debug.Log("CreateNewGameStruct " + dataStruct.blobert_aID.Hex());
        Debug.Log("CreateNewGameStruct " + dataStruct.blobert_bID.Hex());

        Debug.Log("CreateNewGameStruct " + endpointData.functionName);
        Debug.Log("CreateNewGameStruct " + endpointData.addressOfSystem);

        try
        {
            var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
            {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                       dataStruct.player_a.Inner,
                       dataStruct.player_b.Inner,
                       dataStruct.blobert_aID.Inner,
                       dataStruct.blobert_bID.Inner,
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
            });

            return transaction;
        }
        catch (Exception ex)
        {
            Debug.Log("issue with CreateNEwGame" + ex.Message);
            return null;
        }
    }

    public static async Task<FieldElement> CreateCommitTransaction(CommitMoveStruct dataStruct, EndpointDojoCallStruct endpointData)
    {
        try
        {
            Debug.Log(endpointData.functionName);
            Debug.Log(endpointData.addressOfSystem);

            Debug.Log(dataStruct.combat_id.Hex());
            Debug.Log(dataStruct.hash.Hex());

            var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
            {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                       dataStruct.combat_id.Inner,
                       dataStruct.hash.Inner,
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
            });

            return transaction;
        }
        catch (Exception ex)
        {
            Debug.Log("issue with CreateCommitTransaction " + ex.Message);
            return null;
        }
    }

    public static async Task<FieldElement> CreateRevealTransaction(RevealMoveStruct dataStruct, EndpointDojoCallStruct endpointData)
    {
        try
        {
            var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
            {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                       dataStruct.combat_id.Inner,
                       new FieldElement(dataStruct.move).Inner,
                       dataStruct.salt.Inner,
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
            });

            return transaction;
        }
        catch (Exception ex)
        {
            Debug.Log("issue with CreateRevealTransaction" + ex.Message);
            return null;
        }
    }

    #endregion

}