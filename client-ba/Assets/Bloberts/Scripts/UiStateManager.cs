using QueryStructure;
using SimpleGraphQL;
using System;
using System.Collections.Generic;
using UnityEngine;

public class UiStateManager : MonoBehaviour
{
    //public bool simpleLeaderboardModes = true;
    public GameManager gameManager;

    private void Awake()
    {
        DojoEntitiesStorage.worldManagerData = gameManager.dojoConfig;

        UiReferencesStatic.uiStateManager = this;
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.T))
        {
           //debug.log all the current ent

            if (DojoEntitiesStorage.currentAccount != null)
            {
                Debug.Log("current account is not null");
                Debug.Log(DojoEntitiesStorage.currentAccount.Address.Hex());
            }
            else
            {
                Debug.Log("current account is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.challengeInvite != null)
            {
                Debug.Log("challenge invite is not null");
                Debug.Log(DojoEntitiesStorage.challengeInvite.dojoChallengeId.Hex());
            }
            else
            {
                Debug.Log("challenge invite is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.challengeResponse != null)
            {
                Debug.Log("challenge response is not null");
                Debug.Log(DojoEntitiesStorage.challengeResponse.dojoChallengeId.Hex());
            }
            else
            {
                Debug.Log("challenge response is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.selectedChallengeID != null)
            {
                Debug.Log("selected challenge id is not null");
                Debug.Log(DojoEntitiesStorage.selectedChallengeID.Hex());
            }
            else
            {
                Debug.Log("selected challenge id is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.currentCombatId != null)
            {
                Debug.Log("current round id is not null");
                Debug.Log(DojoEntitiesStorage.currentCombatId.Hex());
            }
            else
            {
                Debug.Log("current round id is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.knockoutCurrentGame != null)
            {
                Debug.Log("knockout current game is not null");
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.dojoCombatId.Hex());
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.dojoBlobertA.Hex() + " blob a id");
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.dojoBlobertB.Hex() + " blob b id");
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerA.Hex() + " player a id");
                Debug.Log(DojoEntitiesStorage.knockoutCurrentGame.dojoPlayerB.Hex() + " player b id");
            }
            else
            {
                Debug.Log("knockout current game is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.healthsCurrentGame != null)
            {
                Debug.Log("healths current game is not null");
                Debug.Log(DojoEntitiesStorage.healthsCurrentGame.dojoCombatId.Hex());
                Debug.Log(DojoEntitiesStorage.healthsCurrentGame.dojoA + " health a");
                Debug.Log(DojoEntitiesStorage.healthsCurrentGame.dojoB + " health b");
            }
            else
            {
                Debug.Log("healths current game is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.lastRoundCurrentGame != null)
            {
                Debug.Log("last round current game is not null");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.dojoCombatId.Hex());
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.dojoHealthA + " health a");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.dojoHealthB + " health b");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.dojoMoveA + " move a");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.dojoMoveB + " move b");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.dojoDamageA + " damage a");
                Debug.Log(DojoEntitiesStorage.lastRoundCurrentGame.dojoDamageB + " damage b");
            }
            else
            {
                Debug.Log("last round current game is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.twoHashesCurrentGame != null)
            {
                Debug.Log("two hashes current game is not null");
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.dojoId.Hex());
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.dojoA + " hash a");
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.dojoB + " hash b");
            }
            else
            {
                Debug.Log("two hashes id is null");
            }

            Debug.Log("\n\n");

            if (DojoEntitiesStorage.twoHashesCurrentGame != null)
            {
                Debug.Log("two hashes current game is not null");
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.dojoId.Hex());
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.dojoA + " hash a");
                Debug.Log(DojoEntitiesStorage.twoHashesCurrentGame.dojoB + " hash b");
            }
            else
            {
                Debug.Log("two hashes id is null");
            }

            Debug.Log("\n\n");

            Debug.Log($"this is the amount of invtations in general {DojoEntitiesStorage.challengeInvitesDict.Count}");
            Debug.Log($"this is the amount of invtations for the player {DojoEntitiesStorage.userReceivedChallengeInvites.Count}");
            Debug.Log($"this is the amount of responses for the player {DojoEntitiesStorage.challengeResponseDict.Count}");

            Debug.Log("\n\n");

            Debug.Log($"this is the amount of blobs {DojoEntitiesStorage.allBlobertDict.Count}");
            Debug.Log($"this is the amount of blobs for the player {DojoEntitiesStorage.userBloberts.Count}");
        }

        if (Input.GetKeyDown(KeyCode.O))
        {
            KeyStorageManager.SaveKeyPair(BlobertUtils.Address0sFix(DojoEntitiesStorage.currentAccount.Address.Hex()), DojoEntitiesStorage.currentAccount.Signer.Inner.Hex());
        }

        if (Input.GetKeyDown(KeyCode.P))
        {
            var keys = KeyStorageManager.GetAllKeyPairs();

            Debug.Log("prob a double debug log");
            Debug.Log(keys);
        }
    }



    public async void TestFunction()
    {
        var client = new GraphQLClient($"http://localhost:8080/graphql");


        var blobertGQLNoInput = QueryManagerUtils.QueryNoInput(QueryManagerUtils.blobertGraphQLQuery);



        Debug.Log(blobertGQLNoInput);
        //dictionary of string 
        var variables = new Dictionary<string, string>
        {
            { "id", "\"1\"" },
            {"owner", "\"0x7bb970411262d19d5d9e098a145d4de47a54daef4a547b484b637ecdd39a590\"" }
        };
        var where = QueryManagerUtils.CreateWhereClause(variables);

        var order = QueryManagerUtils.CreateOrderClause(new Dictionary<string, string>
        {
            { "direction", "ASC" },
            { "field", "ID" }
        });
        Debug.Log(order);
        Debug.Log(where);


        var blobertGQLWithInput = QueryManagerUtils.QueryWithInput(QueryManagerUtils.blobertGraphQLQuery, new List<string>
        {
            order,
            where
        });

        Debug.Log(blobertGQLWithInput);
        
        var tradesRequest = new Request
        {
            Query = blobertGQLNoInput,
        };

        var responseType = new
        {
            blobertModels = Models<QueryStructure.BlobertData>.CreateModel(() => new BlobertData
            {
                __typename = "",
                owner = "",
                id = "",
                traits = new QueryStructure.Traits
                {
                    armour = "",
                    background = "",
                    jewelry = "",
                    mask = "",
                    weapon = ""
                },
                stats = new QueryStructure.Stats
                {
                    attack = "",
                    defense = "",
                    speed = "",
                    strength = ""
                }
            })
        };

        var response = await client.Send(() => responseType, tradesRequest);

        //Debug.Log(response.Data.blobertModels);
        //Debug.Log(response.Data.blobertModels);
        //Debug.Log(response.Data.blobertModels.edges[0].Node.Entity.Models[0].owner);

        //var edges = response.Data.blobertModels.edges;

        //for (int i = 0; i < edges.Length; i++)
        //{
        //    var entity = edges[i].Node.Entity;

        //    for (int x = 0; x < entity.Models.Length; x++)
        //    {
        //        if (entity.Models[x].__typename == "Blobert")
        //        {
        //            Debug.Log("there is a blobert");
        //            Debug.Log(entity.Models[x].owner);
        //            Debug.Log(entity.Models[x].id);

        //            Debug.Log("traits");
        //            Debug.Log(entity.Models[x].traits.background);
        //            Debug.Log(entity.Models[x].traits.mask);
        //            Debug.Log(entity.Models[x].traits.weapon);
        //            Debug.Log(entity.Models[x].traits.armour);
        //            Debug.Log(entity.Models[x].traits.jewelry);
                
        //            Debug.Log("stats");
        //            Debug.Log(entity.Models[x].stats.defense);
        //            Debug.Log(entity.Models[x].stats.speed);
        //            Debug.Log(entity.Models[x].stats.attack);
        //            Debug.Log(entity.Models[x].stats.strength);
                    
        //            Debug.Log("\n\n");
        //        }
        //    }
        //}
    }
}



