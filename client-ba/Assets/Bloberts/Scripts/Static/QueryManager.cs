
using System;
using System.Collections.Generic;

namespace QueryStructure
{
    public static class QueryManagerUtils
    {
        public static string ReplaceWords(string input, Dictionary<string, string> replacements)
        {
            foreach (var pair in replacements)
            {
                input = input.Replace(pair.Key, pair.Value);
            }
            return input;
        }

        public static string QueryNoInput(string input)
        {
            return input.Replace("arguments", "");
        }

        public static string QueryWithInput(string input,List<string> clauses)
        {
            var argumentQuery = "(";
            for (int i = 0; i < clauses.Count; i++)
            {
                argumentQuery += clauses[i];
                if (i < clauses.Count - 1)
                {
                    argumentQuery += ", ";
                }
            }
            argumentQuery += ")";
            string query = input.Replace("arguments", argumentQuery);
            return query;
        }

        public static string CreateWhereClause(Dictionary<string, string> replacements)
        {
            string whereClause = "where: {";
            foreach (var pair in replacements)
            {
                whereClause += pair.Key + ": " + pair.Value + ", ";
            }
            whereClause = whereClause.Remove(whereClause.Length - 2);
            whereClause += "}";
            return whereClause;
        }

        public static string CreateOrderClause(Dictionary<string, string> replacements)
        {
            string orderClause = "order: {";
            foreach (var pair in replacements)
            {
                orderClause += pair.Key + ": " + pair.Value + ", ";
            }
            orderClause = orderClause.Remove(orderClause.Length - 2);
            orderClause += "}";
            return orderClause;
        }


        public static readonly string blobertGraphQLQuery = @"query {
      blobertModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on Blobert {
                  id
owner
traits {
background
armour
mask
jewelry
weapon
} 
stats {
attack
defense
speed
strength
} 

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string challengeInviteGraphQLQuery = @"query {
      challengeInviteModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on ChallengeInvite {
                  challenge_id
sender
receiver
blobert_id
open

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string challengeResponseGraphQLQuery = @"query {
      challengeResponseModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on ChallengeResponse {
                  challenge_id
blobert_id
open
combat_id

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string challengeScoreGraphQLQuery = @"query {
      challengeScoreModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on ChallengeScore {
                  player
blobert_id
wins
losses
max_consecutive_wins
current_consecutive_wins

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string twoHashesGraphQLQuery = @"query {
      twoHashesModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on TwoHashes {
                  id
a
b

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string twoMovesGraphQLQuery = @"query {
      twoMovesModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on TwoMoves {
                  id
a 
b 

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string healthsGraphQLQuery = @"query {
      healthsModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on Healths {
                  combat_id
a
b

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string knockoutGraphQLQuery = @"query {
      knockoutModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on Knockout {
                  combat_id
player_a
player_b
blobert_a
blobert_b

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string lastRoundGraphQLQuery = @"query {
      lastRoundModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on LastRound {
                  combat_id
health_a
health_b
move_a 
move_b 
damage_a
damage_b

                }
              }
            }
          }
        }
      }
    }";

        public static readonly string stakeGraphQLQuery = @"query {
      stakeModels arguments {
        edges {
          node {
            entity {
              keys
              models {
                __typename
                ... on Stake {
                  combat_id
amount
blobert

                }
              }
            }
          }
        }
      }
    }";
    }

    public class Traits
    {
        public string background;
        public string armour;
        public string mask;
        public string jewelry;
        public string weapon;

    }

    public class Stats
    {
        public string attack;
        public string defense;
        public string speed;
        public string strength;

    }

    public interface IData
    {
        string __typename { get; set; }
    }

    public class BlobertData : IData
    {
        public string __typename { get; set; }
        public string owner { get; set; }
        public string id { get; set; }
        public Traits traits { get; set; }
        public Stats stats { get; set; }
    }

    public class TradeData : IData
    {
        public string __typename { get; set; }
        public string seller { get; set; }
        public string owner { get; set; }
    }

    public class Entity<T> where T : IData
    {
        public string[] Keys { get; set; }
        public T[] Models { get; set; }
    }

    public class Node<T> where T : IData
    {
        public Entity<T> Entity { get; set; }
    }

    public class Edge<T> where T : IData
    {
        public Node<T> Node { get; set; }
    }

    public class Models<T> where T : IData
    {
        public Edge<T>[] edges { get; set; }

        public static Models<T> CreateModel(Func<T> createData)
        {
            return new Models<T>
            {
                edges = new Edge<T>[]
                {
                new Edge<T>
                {
                    Node = new Node<T>
                    {
                        Entity = new Entity<T>
                        {
                            Keys = new string[] { "" },
                            Models = new T[]
                            {
                                createData()
                            }
                        }
                    }
                }
                }
            };
        }
    }
}
