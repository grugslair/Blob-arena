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

        if (GUI.changed) 
        {
            switch (data.environmentType) 
            {
                case EnvironmentType.LOCAL:

                    data.toriiUrl = "http://localhost:8080";
                    data.rpcUrl = "http://localhost:5050";

                    data.worldAddress = "0x3a0394af68d1727a0019949a94fa584e8bc132903d49bb545888eb1bd427cf4";

                    data.blobertContractAddress = "0x3e2408ea9affd43d731fcb31e67f7c2c6899cef4c1279dc597dc5d14b240d12";
                    data.knockoutContractAddress = "0x66821c7071e66a727918207afb0255e5dac1677b1732a95104c7672fc98d51e";
                    data.challengeblobertContractAddress = "0x3ce2e701b020ba2c2af15b7347c9d05a5f28b7060609295c6f461af326bc68c";
                    data.lobbyContractAddress = "";

                    data.masterAddress = "0xb3ff441a68610b30fd5e2abbf3a1548eb6ba6f3559f2862bf2dc757e5828ca";
                    data.masterPrivateKey = "0x2bbf4f9fd0bbb2e60b0316c1fe0b76cf7a4d0198bd493ced9b8df2a3a24d68a";
                    break;

                case EnvironmentType.TORII:

                    data.toriiUrl = "https://api.cartridge.gg/x/ba/torii";
                    data.rpcUrl = "https://api.cartridge.gg/x/ba/katana";

                    data.worldAddress = "0x3a0394af68d1727a0019949a94fa584e8bc132903d49bb545888eb1bd427cf4";

                    data.blobertContractAddress = "0x3e2408ea9affd43d731fcb31e67f7c2c6899cef4c1279dc597dc5d14b240d12";
                    data.knockoutContractAddress = "0x66821c7071e66a727918207afb0255e5dac1677b1732a95104c7672fc98d51e";
                    data.challengeblobertContractAddress = "0x3ce2e701b020ba2c2af15b7347c9d05a5f28b7060609295c6f461af326bc68c";
                    data.lobbyContractAddress = "";

                    data.masterAddress = "0xdf6a29cf4ffd62158f8b39fd3b705c13d34932632b22994f143428ca303871";
                    data.masterPrivateKey = "0x1d153b36b2649e1e273a6dfd3a2ede98419b0dcc7e2a32e20bbee7df083f49c";
                    break;

                case EnvironmentType.TESTNET:

                    data.toriiUrl = "";
                    data.rpcUrl = "";

                    data.worldAddress = "0x6907ac71d377de72deae6cf331d2bbfabc644441916c3f8c307074cf1195d11";

                    data.blobertContractAddress = "";
                    data.knockoutContractAddress = "";
                    data.challengeblobertContractAddress = "";
                    data.lobbyContractAddress = "";

                    data.masterAddress = "";
                    data.masterPrivateKey = "";

                    break;

                case EnvironmentType.MAINNET:

                    data.toriiUrl = "";
                    data.rpcUrl = "";

                    data.worldAddress = "0x6907ac71d377de72deae6cf331d2bbfabc644441916c3f8c307074cf1195d11";

                    data.blobertContractAddress = "";
                    data.knockoutContractAddress = "";
                    data.challengeblobertContractAddress = "";
                    data.lobbyContractAddress = "";

                    data.masterAddress = "";
                    data.masterPrivateKey = "";

                    break;
            }

            EditorUtility.SetDirty(data); 
        }
    }
}
