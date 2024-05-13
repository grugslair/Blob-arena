using UnityEngine;
using UnityEditor;
using Dojo;

[CustomEditor(typeof(WorldManagerData))]
public class WorldManagerDataEditor : Editor
{
    public override void OnInspectorGUI()
    {
        base.OnInspectorGUI();

        WorldManagerData data = (WorldManagerData)target;

        if (GUILayout.Button("Refresh"))
        {
            UpdateDataBasedOnEnvironment(data);
        }

        if (GUI.changed)
        {
            UpdateDataBasedOnEnvironment(data);
        }
    }

    private void UpdateDataBasedOnEnvironment(WorldManagerData data)
    {
        switch (data.environmentType)
        {
            case EnvironmentType.LOCAL:

                data.toriiUrl = "http://localhost:8080";
                data.rpcUrl = "http://localhost:5050";

                data.worldAddress = "0x3f70f03ea1f909e8f20d071de49376e0a84aa411b7ae91349dc3c8316e74cb3";

                data.blobertContractAddress = "0xf5eb3ac756b7779a4e117ed03eba91b4e92de72b9b2d3987ee81a3b314540d";
                //data.knockoutContractAddress = "0x66821c7071e66a727918207afb0255e5dac1677b1732a95104c7672fc98d51e";
                data.challengeblobertContractAddress = "0x22749e7dcc2a4c1df19e32c0882bcc3dffe2d38ddd46a378bd130e708565afc";
                data.lobbyContractAddress = "";

                data.masterAddress = "0xb3ff441a68610b30fd5e2abbf3a1548eb6ba6f3559f2862bf2dc757e5828ca";
                data.masterPrivateKey = "0x2bbf4f9fd0bbb2e60b0316c1fe0b76cf7a4d0198bd493ced9b8df2a3a24d68a";
                break;

            case EnvironmentType.TORII:

                data.toriiUrl = "https://api.cartridge.gg/x/ba/torii";
                data.rpcUrl = "https://api.cartridge.gg/x/ba/katana";

                data.worldAddress = "0x3a0394af68d1727a0019949a94fa584e8bc132903d49bb545888eb1bd427cf4";

                data.blobertContractAddress = "0x3e2408ea9affd43d731fcb31e67f7c2c6899cef4c1279dc597dc5d14b240d12";
                //data.knockoutContractAddress = "0x66821c7071e66a727918207afb0255e5dac1677b1732a95104c7672fc98d51e";
                data.challengeblobertContractAddress = "0x3ce2e701b020ba2c2af15b7347c9d05a5f28b7060609295c6f461af326bc68c";
                data.lobbyContractAddress = "";

                data.masterAddress = "0x3698adbdbf29cea0554a534b1596f26e49f885f43e123e62c7d8a6c9d2f6d";
                data.masterPrivateKey = "0x38d81b1d9e837ddd593901c6112925b7be7fdcd411509317357960ca161a67f";
                break;

            case EnvironmentType.TESTNET:

                data.toriiUrl = "https://api.cartridge.gg/x/sepba61/torii";
                data.rpcUrl = "https://starknet-sepolia.public.blastapi.io/rpc/v0_6";

                data.worldAddress = "0x6907ac71d377de72deae6cf331d2bbfabc644441916c3f8c307074cf1195d11";

                data.blobertContractAddress = "0x474ab654b74a42e0923f8a8df15df59301b2a20541707d6c17e777b309256c1";
                //data.knockoutContractAddress = "";
                data.challengeblobertContractAddress = "0x3269c9830a5958f8a68fa415702f11553586be83707c35fd3d7b20f60271781";
                data.lobbyContractAddress = "";

                data.masterAddress = "";
                data.masterPrivateKey = "";

                break;

            case EnvironmentType.MAINNET:

                data.toriiUrl = "";
                data.rpcUrl = "";

                data.worldAddress = "0x6907ac71d377de72deae6cf331d2bbfabc644441916c3f8c307074cf1195d11";

                data.blobertContractAddress = "";
                //data.knockoutContractAddress = "";
                data.challengeblobertContractAddress = "";
                data.lobbyContractAddress = "";

                data.masterAddress = "";
                data.masterPrivateKey = "";

                break;
        }

        EditorUtility.SetDirty(data);
    }
}