from string import Template
import json
from typing import List
from string import Template
import os


MANIFEST_RR = """
{
  "world": {
    "kind": "Contract",
    "class_hash": "0x799bc4e9da10bfb3dd88e6f223c9cfbf7745435cd14f5d69675ea448e578cd",
    "original_class_hash": "0x799bc4e9da10bfb3dd88e6f223c9cfbf7745435cd14f5d69675ea448e578cd",
    "abi": [
      {
        "type": "impl",
        "name": "World",
        "interface_name": "dojo::world::IWorld"
      },
      {
        "type": "struct",
        "name": "core::array::Span::<core::felt252>",
        "members": [
          {
            "name": "snapshot",
            "type": "@core::array::Array::<core::felt252>"
          }
        ]
      },
      {
        "type": "struct",
        "name": "dojo::resource_metadata::ResourceMetadata",
        "members": [
          {
            "name": "resource_id",
            "type": "core::felt252"
          },
          {
            "name": "metadata_uri",
            "type": "core::array::Span::<core::felt252>"
          }
        ]
      },
      {
        "type": "struct",
        "name": "core::array::Span::<core::integer::u8>",
        "members": [
          {
            "name": "snapshot",
            "type": "@core::array::Array::<core::integer::u8>"
          }
        ]
      },
      {
        "type": "enum",
        "name": "core::bool",
        "variants": [
          {
            "name": "False",
            "type": "()"
          },
          {
            "name": "True",
            "type": "()"
          }
        ]
      },
      {
        "type": "interface",
        "name": "dojo::world::IWorld",
        "items": [
          {
            "type": "function",
            "name": "metadata",
            "inputs": [
              {
                "name": "resource_id",
                "type": "core::felt252"
              }
            ],
            "outputs": [
              {
                "type": "dojo::resource_metadata::ResourceMetadata"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "set_metadata",
            "inputs": [
              {
                "name": "metadata",
                "type": "dojo::resource_metadata::ResourceMetadata"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "model",
            "inputs": [
              {
                "name": "name",
                "type": "core::felt252"
              }
            ],
            "outputs": [
              {
                "type": "(core::starknet::class_hash::ClassHash, core::starknet::contract_address::ContractAddress)"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "register_model",
            "inputs": [
              {
                "name": "class_hash",
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "deploy_contract",
            "inputs": [
              {
                "name": "salt",
                "type": "core::felt252"
              },
              {
                "name": "class_hash",
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "outputs": [
              {
                "type": "core::starknet::contract_address::ContractAddress"
              }
            ],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "upgrade_contract",
            "inputs": [
              {
                "name": "address",
                "type": "core::starknet::contract_address::ContractAddress"
              },
              {
                "name": "class_hash",
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "outputs": [
              {
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "uuid",
            "inputs": [],
            "outputs": [
              {
                "type": "core::integer::u32"
              }
            ],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "emit",
            "inputs": [
              {
                "name": "keys",
                "type": "core::array::Array::<core::felt252>"
              },
              {
                "name": "values",
                "type": "core::array::Span::<core::felt252>"
              }
            ],
            "outputs": [],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "entity",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "keys",
                "type": "core::array::Span::<core::felt252>"
              },
              {
                "name": "layout",
                "type": "core::array::Span::<core::integer::u8>"
              }
            ],
            "outputs": [
              {
                "type": "core::array::Span::<core::felt252>"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "set_entity",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "keys",
                "type": "core::array::Span::<core::felt252>"
              },
              {
                "name": "values",
                "type": "core::array::Span::<core::felt252>"
              },
              {
                "name": "layout",
                "type": "core::array::Span::<core::integer::u8>"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "base",
            "inputs": [],
            "outputs": [
              {
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "delete_entity",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "keys",
                "type": "core::array::Span::<core::felt252>"
              },
              {
                "name": "layout",
                "type": "core::array::Span::<core::integer::u8>"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "is_owner",
            "inputs": [
              {
                "name": "address",
                "type": "core::starknet::contract_address::ContractAddress"
              },
              {
                "name": "resource",
                "type": "core::felt252"
              }
            ],
            "outputs": [
              {
                "type": "core::bool"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "grant_owner",
            "inputs": [
              {
                "name": "address",
                "type": "core::starknet::contract_address::ContractAddress"
              },
              {
                "name": "resource",
                "type": "core::felt252"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "revoke_owner",
            "inputs": [
              {
                "name": "address",
                "type": "core::starknet::contract_address::ContractAddress"
              },
              {
                "name": "resource",
                "type": "core::felt252"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "is_writer",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "system",
                "type": "core::starknet::contract_address::ContractAddress"
              }
            ],
            "outputs": [
              {
                "type": "core::bool"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "grant_writer",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "system",
                "type": "core::starknet::contract_address::ContractAddress"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "revoke_writer",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "system",
                "type": "core::starknet::contract_address::ContractAddress"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          }
        ]
      },
      {
        "type": "impl",
        "name": "UpgradeableWorld",
        "interface_name": "dojo::world::IUpgradeableWorld"
      },
      {
        "type": "interface",
        "name": "dojo::world::IUpgradeableWorld",
        "items": [
          {
            "type": "function",
            "name": "upgrade",
            "inputs": [
              {
                "name": "new_class_hash",
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          }
        ]
      },
      {
        "type": "constructor",
        "name": "constructor",
        "inputs": [
          {
            "name": "contract_base",
            "type": "core::starknet::class_hash::ClassHash"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::WorldSpawned",
        "kind": "struct",
        "members": [
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          },
          {
            "name": "creator",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::ContractDeployed",
        "kind": "struct",
        "members": [
          {
            "name": "salt",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          },
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::ContractUpgraded",
        "kind": "struct",
        "members": [
          {
            "name": "class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          },
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::WorldUpgraded",
        "kind": "struct",
        "members": [
          {
            "name": "class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::MetadataUpdate",
        "kind": "struct",
        "members": [
          {
            "name": "resource",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "uri",
            "type": "core::array::Span::<core::felt252>",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::ModelRegistered",
        "kind": "struct",
        "members": [
          {
            "name": "name",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          },
          {
            "name": "prev_class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          },
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          },
          {
            "name": "prev_address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::StoreSetRecord",
        "kind": "struct",
        "members": [
          {
            "name": "table",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "keys",
            "type": "core::array::Span::<core::felt252>",
            "kind": "data"
          },
          {
            "name": "values",
            "type": "core::array::Span::<core::felt252>",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::StoreDelRecord",
        "kind": "struct",
        "members": [
          {
            "name": "table",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "keys",
            "type": "core::array::Span::<core::felt252>",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::WriterUpdated",
        "kind": "struct",
        "members": [
          {
            "name": "model",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "system",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          },
          {
            "name": "value",
            "type": "core::bool",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::OwnerUpdated",
        "kind": "struct",
        "members": [
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          },
          {
            "name": "resource",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "value",
            "type": "core::bool",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::Event",
        "kind": "enum",
        "variants": [
          {
            "name": "WorldSpawned",
            "type": "dojo::world::world::WorldSpawned",
            "kind": "nested"
          },
          {
            "name": "ContractDeployed",
            "type": "dojo::world::world::ContractDeployed",
            "kind": "nested"
          },
          {
            "name": "ContractUpgraded",
            "type": "dojo::world::world::ContractUpgraded",
            "kind": "nested"
          },
          {
            "name": "WorldUpgraded",
            "type": "dojo::world::world::WorldUpgraded",
            "kind": "nested"
          },
          {
            "name": "MetadataUpdate",
            "type": "dojo::world::world::MetadataUpdate",
            "kind": "nested"
          },
          {
            "name": "ModelRegistered",
            "type": "dojo::world::world::ModelRegistered",
            "kind": "nested"
          },
          {
            "name": "StoreSetRecord",
            "type": "dojo::world::world::StoreSetRecord",
            "kind": "nested"
          },
          {
            "name": "StoreDelRecord",
            "type": "dojo::world::world::StoreDelRecord",
            "kind": "nested"
          },
          {
            "name": "WriterUpdated",
            "type": "dojo::world::world::WriterUpdated",
            "kind": "nested"
          },
          {
            "name": "OwnerUpdated",
            "type": "dojo::world::world::OwnerUpdated",
            "kind": "nested"
          }
        ]
      }
    ],
    "address": "0x1e56823d2f046537ea7144fa30d5b0d5e411b4714ff3e670447301fd1b24363",
    "transaction_hash": "0x11a36ed552ec26440c2be4693e0327a669bc02ee203c7d5dbd191d3926f769e",
    "block_number": null,
    "seed": "rrseptwo",
    "name": "dojo::world::world"
  },
  "base": {
    "kind": "Class",
    "class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
    "original_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
    "abi": null,
    "name": "dojo::base::base"
  },
  "contracts": [
    {
      "kind": "DojoContract",
      "address": "0x6de9cefe48e17d383876e62233e5271f5cb7ef985fc7139a1c4b902db4046c2",
      "class_hash": "0x634c1bbf3d2854b615656797e1aeb38de882c58aa82ed8553af5b16e47267c8",
      "original_class_hash": "0x634c1bbf3d2854b615656797e1aeb38de882c58aa82ed8553af5b16e47267c8",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "GameActionImpl",
          "interface_name": "risingrevenant::contracts::game::IGameActions"
        },
        {
          "type": "interface",
          "name": "risingrevenant::contracts::game::IGameActions",
          "items": [
            {
              "type": "function",
              "name": "create",
              "inputs": [
                {
                  "name": "start_block",
                  "type": "core::integer::u64"
                },
                {
                  "name": "preparation_blocks",
                  "type": "core::integer::u64"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u128"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::contracts::game::game_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "risingrevenant::contracts::game::game_actions"
    },
    {
      "kind": "DojoContract",
      "address": "0x33b1c476eaa48aa39c8f145c77a05da2f7effa2cd2eea486dc71d4b4409eccd",
      "class_hash": "0x4a7c0668e223b74a62dcc51dbaecf6e251b1610090433af591a531c976540b4",
      "original_class_hash": "0x4a7c0668e223b74a62dcc51dbaecf6e251b1610090433af591a531c976540b4",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "OutpostActionsImpl",
          "interface_name": "risingrevenant::contracts::outpost::IOutpostActions"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::Position",
          "members": [
            {
              "name": "x",
              "type": "core::integer::u32"
            },
            {
              "name": "y",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::integer::u256",
          "members": [
            {
              "name": "low",
              "type": "core::integer::u128"
            },
            {
              "name": "high",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "enum",
          "name": "risingrevenant::components::reinforcement::ReinforcementType",
          "variants": [
            {
              "name": "None",
              "type": "()"
            },
            {
              "name": "Wall",
              "type": "()"
            },
            {
              "name": "Trench",
              "type": "()"
            },
            {
              "name": "Bunker",
              "type": "()"
            }
          ]
        },
        {
          "type": "enum",
          "name": "risingrevenant::components::outpost::OutpostEventStatus",
          "variants": [
            {
              "name": "NotImpacted",
              "type": "()"
            },
            {
              "name": "UnVerified",
              "type": "()"
            },
            {
              "name": "Verified",
              "type": "()"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::contracts::outpost::IOutpostActions",
          "items": [
            {
              "type": "function",
              "name": "purchase",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [
                {
                  "type": "risingrevenant::components::game::Position"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "get_price",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u256"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "reinforce",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "outpost_id",
                  "type": "risingrevenant::components::game::Position"
                },
                {
                  "name": "count",
                  "type": "core::integer::u32"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "verify",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "outpost_id",
                  "type": "risingrevenant::components::game::Position"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "set_reinforcement_type",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "outpost_id",
                  "type": "risingrevenant::components::game::Position"
                },
                {
                  "name": "reinforcement_type",
                  "type": "risingrevenant::components::reinforcement::ReinforcementType"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "get_event_status",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "outpost_id",
                  "type": "risingrevenant::components::game::Position"
                }
              ],
              "outputs": [
                {
                  "type": "risingrevenant::components::outpost::OutpostEventStatus"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::contracts::outpost::outpost_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "risingrevenant::contracts::outpost::outpost_actions"
    },
    {
      "kind": "DojoContract",
      "address": "0x2c3f97685ac5cded89b53037efe8353ce9481cdf74fb10bacaccbeb23825f7a",
      "class_hash": "0x7fec82e97eef38c1e77c0f775f3fd2f6ed1c8738a9257f8e1f52b883b401d0b",
      "original_class_hash": "0x7fec82e97eef38c1e77c0f775f3fd2f6ed1c8738a9257f8e1f52b883b401d0b",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "PaymentActionsImpl",
          "interface_name": "risingrevenant::contracts::payment::IPaymentActions"
        },
        {
          "type": "interface",
          "name": "risingrevenant::contracts::payment::IPaymentActions",
          "items": [
            {
              "type": "function",
              "name": "claim_jackpot",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "claim_confirmation_contribution",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::contracts::payment::payment_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "risingrevenant::contracts::payment::payment_actions"
    },
    {
      "kind": "DojoContract",
      "address": "0x6784d9efb5aac9f731b8acb9a8dd2be1d2e5da6435eba6a6587d7c69a3f03f5",
      "class_hash": "0x3e2736c03ea5ae58fb56abb63b67153670796b16436f4a74fa1e36e925e06ac",
      "original_class_hash": "0x3e2736c03ea5ae58fb56abb63b67153670796b16436f4a74fa1e36e925e06ac",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "ReinforcementActionsImpl",
          "interface_name": "risingrevenant::contracts::reinforcement::IReinforcementActions"
        },
        {
          "type": "interface",
          "name": "risingrevenant::contracts::reinforcement::IReinforcementActions",
          "items": [
            {
              "type": "function",
              "name": "get_price",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "count",
                  "type": "core::integer::u32"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u128"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "purchase",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "count",
                  "type": "core::integer::u32"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::contracts::reinforcement::reinforcement_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "risingrevenant::contracts::reinforcement::reinforcement_actions"
    },
    {
      "kind": "DojoContract",
      "address": "0x508695fbf91aeacaf6b711046bd41225d3c8d448b368ee22c4cb4ee280c861d",
      "class_hash": "0x2d042c017417dea4778e5c5afff4e926f958552300e4160b216b4512fc3f4d",
      "original_class_hash": "0x2d042c017417dea4778e5c5afff4e926f958552300e4160b216b4512fc3f4d",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "TradeOutpostActionImpl",
          "interface_name": "risingrevenant::contracts::trade_outpost::ITradeOutpostActions"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::Position",
          "members": [
            {
              "name": "x",
              "type": "core::integer::u32"
            },
            {
              "name": "y",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::contracts::trade_outpost::ITradeOutpostActions",
          "items": [
            {
              "type": "function",
              "name": "create",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "price",
                  "type": "core::integer::u128"
                },
                {
                  "name": "outpost_id",
                  "type": "risingrevenant::components::game::Position"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u128"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "revoke",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "trade_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "purchase",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "trade_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "modify_price",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "trade_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "new_price",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "get_status",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "trade_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u8"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::contracts::trade_outpost::trade_outpost_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "risingrevenant::contracts::trade_outpost::trade_outpost_actions"
    },
    {
      "kind": "DojoContract",
      "address": "0x2203ce9ad61203364cf2ccca067b248c55d8b840772c9da6ead45212906a4ac",
      "class_hash": "0xc4b3ccb13d3685483a194c53296e52f7ac28d8dc2d4aa264128ffd61e5c569",
      "original_class_hash": "0xc4b3ccb13d3685483a194c53296e52f7ac28d8dc2d4aa264128ffd61e5c569",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "TradeReinforcementsActionsImpl",
          "interface_name": "risingrevenant::contracts::trade_reinforcement::ITradeReinforcementsActions"
        },
        {
          "type": "interface",
          "name": "risingrevenant::contracts::trade_reinforcement::ITradeReinforcementsActions",
          "items": [
            {
              "type": "function",
              "name": "create",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "price",
                  "type": "core::integer::u128"
                },
                {
                  "name": "count",
                  "type": "core::integer::u32"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u128"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "revoke",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "trade_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "purchase",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "trade_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "modify_price",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "trade_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "new_price",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "get_status",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "trade_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u8"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::contracts::trade_reinforcement::trade_reinforcement_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "risingrevenant::contracts::trade_reinforcement::trade_reinforcement_actions"
    },
    {
      "kind": "DojoContract",
      "address": "0x235e8588ab24b17322ac3e05611338638dcd2e868c96a504648b6ce7a16eea",
      "class_hash": "0x4f602cbe34cc87297f3d756a815ac742a618a227dd32e213d3c7334ddf54c75",
      "original_class_hash": "0x4f602cbe34cc87297f3d756a815ac742a618a227dd32e213d3c7334ddf54c75",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldEventActionImpl",
          "interface_name": "risingrevenant::contracts::world_event::IWorldEventActions"
        },
        {
          "type": "interface",
          "name": "risingrevenant::contracts::world_event::IWorldEventActions",
          "items": [
            {
              "type": "function",
              "name": "random",
              "inputs": [
                {
                  "name": "game_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u128"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::contracts::world_event::world_event_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "risingrevenant::contracts::world_event::world_event_actions"
    }
  ],
  "models": [
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "owner",
          "type": "ContractAddress",
          "key": true
        },
        {
          "name": "game_id",
          "type": "u128",
          "key": false
        }
      ],
      "class_hash": "0x4242ca092ea88998c8bda08f2a54d21f79ab68f000545951c6ef4193f7017d0",
      "original_class_hash": "0x4242ca092ea88998c8bda08f2a54d21f79ab68f000545951c6ef4193f7017d0",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "current_gameImpl",
          "interface_name": "risingrevenant::components::game::Icurrent_game"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::CurrentGame",
          "members": [
            {
              "name": "owner",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "game_id",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Icurrent_game",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::CurrentGame"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::current_game::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::current_game"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "owner",
          "type": "ContractAddress",
          "key": true
        },
        {
          "name": "balance",
          "type": "u256",
          "key": false
        },
        {
          "name": "init",
          "type": "bool",
          "key": false
        }
      ],
      "class_hash": "0x26441cc27c0f41db9575e0ff584da692151244f8bd9f2ddecfedddd601503b9",
      "original_class_hash": "0x26441cc27c0f41db9575e0ff584da692151244f8bd9f2ddecfedddd601503b9",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "dev_walletImpl",
          "interface_name": "risingrevenant::components::game::Idev_wallet"
        },
        {
          "type": "struct",
          "name": "core::integer::u256",
          "members": [
            {
              "name": "low",
              "type": "core::integer::u128"
            },
            {
              "name": "high",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "enum",
          "name": "core::bool",
          "variants": [
            {
              "name": "False",
              "type": "()"
            },
            {
              "name": "True",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::DevWallet",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "owner",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "balance",
              "type": "core::integer::u256"
            },
            {
              "name": "init",
              "type": "core::bool"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Idev_wallet",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::DevWallet"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::dev_wallet::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::dev_wallet"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "address",
          "type": "ContractAddress",
          "key": false
        }
      ],
      "class_hash": "0x4d9d2a1b9174414cd4e13e8a3a33959bc18d58323c6a3b104d79972e28f208",
      "original_class_hash": "0x4d9d2a1b9174414cd4e13e8a3a33959bc18d58323c6a3b104d79972e28f208",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "game_erc_20Impl",
          "interface_name": "risingrevenant::components::game::Igame_erc_20"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::GameERC20",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Igame_erc_20",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::GameERC20"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::game_erc_20::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::game_erc_20"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "dimensions",
          "type": "Dimensions",
          "key": false
        }
      ],
      "class_hash": "0xa7aac30a611ed005ac6a32937881ab5cacbd5903b4693bba8402349e276780",
      "original_class_hash": "0xa7aac30a611ed005ac6a32937881ab5cacbd5903b4693bba8402349e276780",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "game_mapImpl",
          "interface_name": "risingrevenant::components::game::Igame_map"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::Dimensions",
          "members": [
            {
              "name": "x",
              "type": "core::integer::u32"
            },
            {
              "name": "y",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::GameMap",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "dimensions",
              "type": "risingrevenant::components::game::Dimensions"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Igame_map",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::GameMap"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::game_map::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::game_map"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "status",
          "type": "u8",
          "key": false
        },
        {
          "name": "preparation_block_number",
          "type": "u64",
          "key": false
        },
        {
          "name": "play_block_number",
          "type": "u64",
          "key": false
        }
      ],
      "class_hash": "0x4ecdfc1dc1740525c5b300cfe02d4b1f1a8ee4801d7e9318ff4206d4c8ad77d",
      "original_class_hash": "0x4ecdfc1dc1740525c5b300cfe02d4b1f1a8ee4801d7e9318ff4206d4c8ad77d",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "game_phasesImpl",
          "interface_name": "risingrevenant::components::game::Igame_phases"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::GamePhases",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "status",
              "type": "core::integer::u8"
            },
            {
              "name": "preparation_block_number",
              "type": "core::integer::u64"
            },
            {
              "name": "play_block_number",
              "type": "core::integer::u64"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Igame_phases",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::GamePhases"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::game_phases::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::game_phases"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "total_pot",
          "type": "u256",
          "key": false
        },
        {
          "name": "winners_pot",
          "type": "u256",
          "key": false
        },
        {
          "name": "confirmation_pot",
          "type": "u256",
          "key": false
        },
        {
          "name": "ltr_pot",
          "type": "u256",
          "key": false
        },
        {
          "name": "dev_pot",
          "type": "u256",
          "key": false
        },
        {
          "name": "claimed",
          "type": "bool",
          "key": false
        }
      ],
      "class_hash": "0x3391d9f47d85364bafd0b133e15f4410e46cd230dc727743bee6d429efd255",
      "original_class_hash": "0x3391d9f47d85364bafd0b133e15f4410e46cd230dc727743bee6d429efd255",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "game_potImpl",
          "interface_name": "risingrevenant::components::game::Igame_pot"
        },
        {
          "type": "struct",
          "name": "core::integer::u256",
          "members": [
            {
              "name": "low",
              "type": "core::integer::u128"
            },
            {
              "name": "high",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "enum",
          "name": "core::bool",
          "variants": [
            {
              "name": "False",
              "type": "()"
            },
            {
              "name": "True",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::GamePot",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "total_pot",
              "type": "core::integer::u256"
            },
            {
              "name": "winners_pot",
              "type": "core::integer::u256"
            },
            {
              "name": "confirmation_pot",
              "type": "core::integer::u256"
            },
            {
              "name": "ltr_pot",
              "type": "core::integer::u256"
            },
            {
              "name": "dev_pot",
              "type": "core::integer::u256"
            },
            {
              "name": "claimed",
              "type": "core::bool"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Igame_pot",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::GamePot"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::game_pot::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::game_pot"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "pot_address",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "dev_percent",
          "type": "u8",
          "key": false
        },
        {
          "name": "confirmation_percent",
          "type": "u8",
          "key": false
        },
        {
          "name": "ltr_percent",
          "type": "u8",
          "key": false
        }
      ],
      "class_hash": "0x5f756d32677a32e19a8dade4c8d813d8db03248ea1864c63bb1362733f33cf1",
      "original_class_hash": "0x5f756d32677a32e19a8dade4c8d813d8db03248ea1864c63bb1362733f33cf1",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "game_pot_constsImpl",
          "interface_name": "risingrevenant::components::game::Igame_pot_consts"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::GamePotConsts",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "pot_address",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "dev_percent",
              "type": "core::integer::u8"
            },
            {
              "name": "confirmation_percent",
              "type": "core::integer::u8"
            },
            {
              "name": "ltr_percent",
              "type": "core::integer::u8"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Igame_pot_consts",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::GamePotConsts"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::game_pot_consts::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::game_pot_consts"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "outpost_created_count",
          "type": "u32",
          "key": false
        },
        {
          "name": "outpost_remaining_count",
          "type": "u32",
          "key": false
        },
        {
          "name": "remain_life_count",
          "type": "u32",
          "key": false
        },
        {
          "name": "reinforcement_count",
          "type": "u32",
          "key": false
        },
        {
          "name": "contribution_score_total",
          "type": "u256",
          "key": false
        }
      ],
      "class_hash": "0x63f34e6e8ec91697055df6b5ae9afb4a7d5f31e424684f700feb0c5be97e21b",
      "original_class_hash": "0x63f34e6e8ec91697055df6b5ae9afb4a7d5f31e424684f700feb0c5be97e21b",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "game_stateImpl",
          "interface_name": "risingrevenant::components::game::Igame_state"
        },
        {
          "type": "struct",
          "name": "core::integer::u256",
          "members": [
            {
              "name": "low",
              "type": "core::integer::u128"
            },
            {
              "name": "high",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::GameState",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "outpost_created_count",
              "type": "core::integer::u32"
            },
            {
              "name": "outpost_remaining_count",
              "type": "core::integer::u32"
            },
            {
              "name": "remain_life_count",
              "type": "core::integer::u32"
            },
            {
              "name": "reinforcement_count",
              "type": "core::integer::u32"
            },
            {
              "name": "contribution_score_total",
              "type": "core::integer::u256"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Igame_state",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::GameState"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::game_state::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::game_state"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "trade_tax_percent",
          "type": "u8",
          "key": false
        }
      ],
      "class_hash": "0x5704bba20051dfb1bb89adf5c9f87be40928903b990fd2a8db1b8a0a56f4c4f",
      "original_class_hash": "0x5704bba20051dfb1bb89adf5c9f87be40928903b990fd2a8db1b8a0a56f4c4f",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "game_trade_taxImpl",
          "interface_name": "risingrevenant::components::game::Igame_trade_tax"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::GameTradeTax",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "trade_tax_percent",
              "type": "core::integer::u8"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::game::Igame_trade_tax",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::game::GameTradeTax"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::game::game_trade_tax::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::game::game_trade_tax"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "position",
          "type": "Position",
          "key": true
        },
        {
          "name": "owner",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "life",
          "type": "u32",
          "key": false
        },
        {
          "name": "reinforces_remaining",
          "type": "u32",
          "key": false
        },
        {
          "name": "reinforcement_type",
          "type": "ReinforcementType",
          "key": false
        },
        {
          "name": "status",
          "type": "u8",
          "key": false
        }
      ],
      "class_hash": "0x9b00e21ac3c2e4ebd4f2c3ad75dcd9e3d141708c6f92ba61c5d8d448089d11",
      "original_class_hash": "0x9b00e21ac3c2e4ebd4f2c3ad75dcd9e3d141708c6f92ba61c5d8d448089d11",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "outpostImpl",
          "interface_name": "risingrevenant::components::outpost::Ioutpost"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::Position",
          "members": [
            {
              "name": "x",
              "type": "core::integer::u32"
            },
            {
              "name": "y",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "enum",
          "name": "risingrevenant::components::reinforcement::ReinforcementType",
          "variants": [
            {
              "name": "None",
              "type": "()"
            },
            {
              "name": "Wall",
              "type": "()"
            },
            {
              "name": "Trench",
              "type": "()"
            },
            {
              "name": "Bunker",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::outpost::Outpost",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "position",
              "type": "risingrevenant::components::game::Position"
            },
            {
              "name": "owner",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "life",
              "type": "core::integer::u32"
            },
            {
              "name": "reinforces_remaining",
              "type": "core::integer::u32"
            },
            {
              "name": "reinforcement_type",
              "type": "risingrevenant::components::reinforcement::ReinforcementType"
            },
            {
              "name": "status",
              "type": "core::integer::u8"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::outpost::Ioutpost",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::outpost::Outpost"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::outpost::outpost::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::outpost::outpost"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "price",
          "type": "u256",
          "key": false
        },
        {
          "name": "available",
          "type": "u32",
          "key": false
        }
      ],
      "class_hash": "0x22070a67e875480903780f820a138952f9e33ea67c8fa031e475024219532af",
      "original_class_hash": "0x22070a67e875480903780f820a138952f9e33ea67c8fa031e475024219532af",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "outpost_marketImpl",
          "interface_name": "risingrevenant::components::outpost::Ioutpost_market"
        },
        {
          "type": "struct",
          "name": "core::integer::u256",
          "members": [
            {
              "name": "low",
              "type": "core::integer::u128"
            },
            {
              "name": "high",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::outpost::OutpostMarket",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "price",
              "type": "core::integer::u256"
            },
            {
              "name": "available",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::outpost::Ioutpost_market",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::outpost::OutpostMarket"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::outpost::outpost_market::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::outpost::outpost_market"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "life",
          "type": "u32",
          "key": false
        },
        {
          "name": "max_reinforcements",
          "type": "u32",
          "key": false
        }
      ],
      "class_hash": "0x47367c7805bd93aab8e71f555316d00e35a8c0bec21a95dc4268800a8258795",
      "original_class_hash": "0x47367c7805bd93aab8e71f555316d00e35a8c0bec21a95dc4268800a8258795",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "outpost_setupImpl",
          "interface_name": "risingrevenant::components::outpost::Ioutpost_setup"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::outpost::OutpostSetup",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "life",
              "type": "core::integer::u32"
            },
            {
              "name": "max_reinforcements",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::outpost::Ioutpost_setup",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::outpost::OutpostSetup"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::outpost::outpost_setup::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::outpost::outpost_setup"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "player_id",
          "type": "ContractAddress",
          "key": true
        },
        {
          "name": "score",
          "type": "u256",
          "key": false
        },
        {
          "name": "claimed",
          "type": "bool",
          "key": false
        }
      ],
      "class_hash": "0x670861e9783272818b1c2ad6f58e813528a3e28311ccd0a18e89d0cdabc1d1a",
      "original_class_hash": "0x670861e9783272818b1c2ad6f58e813528a3e28311ccd0a18e89d0cdabc1d1a",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "player_contributionImpl",
          "interface_name": "risingrevenant::components::player::Iplayer_contribution"
        },
        {
          "type": "struct",
          "name": "core::integer::u256",
          "members": [
            {
              "name": "low",
              "type": "core::integer::u128"
            },
            {
              "name": "high",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "enum",
          "name": "core::bool",
          "variants": [
            {
              "name": "False",
              "type": "()"
            },
            {
              "name": "True",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::player::PlayerContribution",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "player_id",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "score",
              "type": "core::integer::u256"
            },
            {
              "name": "claimed",
              "type": "core::bool"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::player::Iplayer_contribution",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::player::PlayerContribution"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::player::player_contribution::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::player::player_contribution"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "player_id",
          "type": "ContractAddress",
          "key": true
        },
        {
          "name": "outpost_count",
          "type": "u32",
          "key": false
        },
        {
          "name": "reinforcements_available_count",
          "type": "u32",
          "key": false
        },
        {
          "name": "init",
          "type": "bool",
          "key": false
        }
      ],
      "class_hash": "0x5ec02415c3c7beefa4733f6c60e92ae74e9145beef8f01264590401d434ef65",
      "original_class_hash": "0x5ec02415c3c7beefa4733f6c60e92ae74e9145beef8f01264590401d434ef65",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "player_infoImpl",
          "interface_name": "risingrevenant::components::player::Iplayer_info"
        },
        {
          "type": "enum",
          "name": "core::bool",
          "variants": [
            {
              "name": "False",
              "type": "()"
            },
            {
              "name": "True",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::player::PlayerInfo",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "player_id",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "outpost_count",
              "type": "core::integer::u32"
            },
            {
              "name": "reinforcements_available_count",
              "type": "core::integer::u32"
            },
            {
              "name": "init",
              "type": "core::bool"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::player::Iplayer_info",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::player::PlayerInfo"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::player::player_info::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::player::player_info"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "target_price",
          "type": "u128",
          "key": false
        },
        {
          "name": "decay_constant_mag",
          "type": "u128",
          "key": false
        },
        {
          "name": "max_sellable",
          "type": "u32",
          "key": false
        },
        {
          "name": "time_scale_mag",
          "type": "u128",
          "key": false
        },
        {
          "name": "start_block_number",
          "type": "u64",
          "key": false
        },
        {
          "name": "sold",
          "type": "u32",
          "key": false
        }
      ],
      "class_hash": "0x1ce6581a9f5ec768547b57114fec3d5a78202393d7c3cb4b5c36ca0bbd6e86e",
      "original_class_hash": "0x1ce6581a9f5ec768547b57114fec3d5a78202393d7c3cb4b5c36ca0bbd6e86e",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "reinforcement_marketImpl",
          "interface_name": "risingrevenant::components::reinforcement::Ireinforcement_market"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::reinforcement::ReinforcementMarket",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "target_price",
              "type": "core::integer::u128"
            },
            {
              "name": "decay_constant_mag",
              "type": "core::integer::u128"
            },
            {
              "name": "max_sellable",
              "type": "core::integer::u32"
            },
            {
              "name": "time_scale_mag",
              "type": "core::integer::u128"
            },
            {
              "name": "start_block_number",
              "type": "core::integer::u64"
            },
            {
              "name": "sold",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::reinforcement::Ireinforcement_market",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::reinforcement::ReinforcementMarket"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::reinforcement::reinforcement_market::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::reinforcement::reinforcement_market"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "trade_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "trade_type",
          "type": "u8",
          "key": false
        },
        {
          "name": "seller",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "buyer",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "price",
          "type": "u128",
          "key": false
        },
        {
          "name": "offer",
          "type": "Position",
          "key": false
        },
        {
          "name": "status",
          "type": "u8",
          "key": false
        }
      ],
      "class_hash": "0xcbcb04fcf6bfb03d030f4799fd917c3ea5966851449ce7c9f77a02f4b7b667",
      "original_class_hash": "0xcbcb04fcf6bfb03d030f4799fd917c3ea5966851449ce7c9f77a02f4b7b667",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "outpost_tradeImpl",
          "interface_name": "risingrevenant::components::trade::Ioutpost_trade"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::Position",
          "members": [
            {
              "name": "x",
              "type": "core::integer::u32"
            },
            {
              "name": "y",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::trade::OutpostTrade",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "trade_id",
              "type": "core::integer::u128"
            },
            {
              "name": "trade_type",
              "type": "core::integer::u8"
            },
            {
              "name": "seller",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "buyer",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "price",
              "type": "core::integer::u128"
            },
            {
              "name": "offer",
              "type": "risingrevenant::components::game::Position"
            },
            {
              "name": "status",
              "type": "core::integer::u8"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::trade::Ioutpost_trade",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::trade::OutpostTrade"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::trade::outpost_trade::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::trade::outpost_trade"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "trade_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "trade_type",
          "type": "u8",
          "key": false
        },
        {
          "name": "seller",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "buyer",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "price",
          "type": "u128",
          "key": false
        },
        {
          "name": "offer",
          "type": "u32",
          "key": false
        },
        {
          "name": "status",
          "type": "u8",
          "key": false
        }
      ],
      "class_hash": "0x2c2e03a19b9b01d6cd27b05e13eac325f7fdd67dbc0b2ff255588d52c6c0956",
      "original_class_hash": "0x2c2e03a19b9b01d6cd27b05e13eac325f7fdd67dbc0b2ff255588d52c6c0956",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "reinforcement_tradeImpl",
          "interface_name": "risingrevenant::components::trade::Ireinforcement_trade"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::trade::ReinforcementTrade",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "trade_id",
              "type": "core::integer::u128"
            },
            {
              "name": "trade_type",
              "type": "core::integer::u8"
            },
            {
              "name": "seller",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "buyer",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "price",
              "type": "core::integer::u128"
            },
            {
              "name": "offer",
              "type": "core::integer::u32"
            },
            {
              "name": "status",
              "type": "core::integer::u8"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::trade::Ireinforcement_trade",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::trade::ReinforcementTrade"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::trade::reinforcement_trade::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::trade::reinforcement_trade"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "event_id",
          "type": "u128",
          "key": false
        },
        {
          "name": "position",
          "type": "Position",
          "key": false
        },
        {
          "name": "event_type",
          "type": "EventType",
          "key": false
        },
        {
          "name": "radius",
          "type": "u32",
          "key": false
        },
        {
          "name": "number",
          "type": "u32",
          "key": false
        },
        {
          "name": "block_number",
          "type": "u64",
          "key": false
        },
        {
          "name": "previous_event",
          "type": "u128",
          "key": false
        }
      ],
      "class_hash": "0x71fce17a566ae8a513b46da672b3520f26b79a40eb7f722ac90fa69e50997ea",
      "original_class_hash": "0x71fce17a566ae8a513b46da672b3520f26b79a40eb7f722ac90fa69e50997ea",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "current_world_eventImpl",
          "interface_name": "risingrevenant::components::world_event::Icurrent_world_event"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::Position",
          "members": [
            {
              "name": "x",
              "type": "core::integer::u32"
            },
            {
              "name": "y",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "enum",
          "name": "risingrevenant::components::world_event::EventType",
          "variants": [
            {
              "name": "None",
              "type": "()"
            },
            {
              "name": "Dragon",
              "type": "()"
            },
            {
              "name": "Goblin",
              "type": "()"
            },
            {
              "name": "Earthquake",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::world_event::CurrentWorldEvent",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "event_id",
              "type": "core::integer::u128"
            },
            {
              "name": "position",
              "type": "risingrevenant::components::game::Position"
            },
            {
              "name": "event_type",
              "type": "risingrevenant::components::world_event::EventType"
            },
            {
              "name": "radius",
              "type": "core::integer::u32"
            },
            {
              "name": "number",
              "type": "core::integer::u32"
            },
            {
              "name": "block_number",
              "type": "core::integer::u64"
            },
            {
              "name": "previous_event",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::world_event::Icurrent_world_event",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::world_event::CurrentWorldEvent"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::world_event::current_world_event::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::world_event::current_world_event"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "event_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "outpost_id",
          "type": "Position",
          "key": true
        },
        {
          "name": "verified",
          "type": "bool",
          "key": false
        }
      ],
      "class_hash": "0x4143d3dfe2e0259292db59d84e3ee488b0e3c4988adb851a3f952443a1cc180",
      "original_class_hash": "0x4143d3dfe2e0259292db59d84e3ee488b0e3c4988adb851a3f952443a1cc180",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "outpost_verifiedImpl",
          "interface_name": "risingrevenant::components::world_event::Ioutpost_verified"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::Position",
          "members": [
            {
              "name": "x",
              "type": "core::integer::u32"
            },
            {
              "name": "y",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "enum",
          "name": "core::bool",
          "variants": [
            {
              "name": "False",
              "type": "()"
            },
            {
              "name": "True",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::world_event::OutpostVerified",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "event_id",
              "type": "core::integer::u128"
            },
            {
              "name": "outpost_id",
              "type": "risingrevenant::components::game::Position"
            },
            {
              "name": "verified",
              "type": "core::bool"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::world_event::Ioutpost_verified",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::world_event::OutpostVerified"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::world_event::outpost_verified::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::world_event::outpost_verified"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "event_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "position",
          "type": "Position",
          "key": false
        },
        {
          "name": "event_type",
          "type": "EventType",
          "key": false
        },
        {
          "name": "radius",
          "type": "u32",
          "key": false
        },
        {
          "name": "number",
          "type": "u32",
          "key": false
        },
        {
          "name": "block_number",
          "type": "u64",
          "key": false
        },
        {
          "name": "previous_event",
          "type": "u128",
          "key": false
        },
        {
          "name": "next_event",
          "type": "u128",
          "key": false
        }
      ],
      "class_hash": "0x1d46d5de6a5a15f8baa182f357066c7eef69abcb03127e2330999acdff85fee",
      "original_class_hash": "0x1d46d5de6a5a15f8baa182f357066c7eef69abcb03127e2330999acdff85fee",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "world_eventImpl",
          "interface_name": "risingrevenant::components::world_event::Iworld_event"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::game::Position",
          "members": [
            {
              "name": "x",
              "type": "core::integer::u32"
            },
            {
              "name": "y",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "enum",
          "name": "risingrevenant::components::world_event::EventType",
          "variants": [
            {
              "name": "None",
              "type": "()"
            },
            {
              "name": "Dragon",
              "type": "()"
            },
            {
              "name": "Goblin",
              "type": "()"
            },
            {
              "name": "Earthquake",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::world_event::WorldEvent",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "event_id",
              "type": "core::integer::u128"
            },
            {
              "name": "position",
              "type": "risingrevenant::components::game::Position"
            },
            {
              "name": "event_type",
              "type": "risingrevenant::components::world_event::EventType"
            },
            {
              "name": "radius",
              "type": "core::integer::u32"
            },
            {
              "name": "number",
              "type": "core::integer::u32"
            },
            {
              "name": "block_number",
              "type": "core::integer::u64"
            },
            {
              "name": "previous_event",
              "type": "core::integer::u128"
            },
            {
              "name": "next_event",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::world_event::Iworld_event",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::world_event::WorldEvent"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::world_event::world_event::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::world_event::world_event"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "game_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "radius_start",
          "type": "u32",
          "key": false
        },
        {
          "name": "radius_increase",
          "type": "u32",
          "key": false
        }
      ],
      "class_hash": "0x68537c39ccb66b52dced140b435edce054164df4f885fe6bde292a1d3767b53",
      "original_class_hash": "0x68537c39ccb66b52dced140b435edce054164df4f885fe6bde292a1d3767b53",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "world_event_setupImpl",
          "interface_name": "risingrevenant::components::world_event::Iworld_event_setup"
        },
        {
          "type": "struct",
          "name": "risingrevenant::components::world_event::WorldEventSetup",
          "members": [
            {
              "name": "game_id",
              "type": "core::integer::u128"
            },
            {
              "name": "radius_start",
              "type": "core::integer::u32"
            },
            {
              "name": "radius_increase",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "risingrevenant::components::world_event::Iworld_event_setup",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "risingrevenant::components::world_event::WorldEventSetup"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "risingrevenant::components::world_event::world_event_setup::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "risingrevenant::components::world_event::world_event_setup"
    }
  ]
}"""

MANIFEST_BA = """
{
  "world": {
    "kind": "Contract",
    "class_hash": "0x799bc4e9da10bfb3dd88e6f223c9cfbf7745435cd14f5d69675ea448e578cd",
    "original_class_hash": "0x799bc4e9da10bfb3dd88e6f223c9cfbf7745435cd14f5d69675ea448e578cd",
    "abi": [
      {
        "type": "impl",
        "name": "World",
        "interface_name": "dojo::world::IWorld"
      },
      {
        "type": "struct",
        "name": "core::array::Span::<core::felt252>",
        "members": [
          {
            "name": "snapshot",
            "type": "@core::array::Array::<core::felt252>"
          }
        ]
      },
      {
        "type": "struct",
        "name": "dojo::resource_metadata::ResourceMetadata",
        "members": [
          {
            "name": "resource_id",
            "type": "core::felt252"
          },
          {
            "name": "metadata_uri",
            "type": "core::array::Span::<core::felt252>"
          }
        ]
      },
      {
        "type": "struct",
        "name": "core::array::Span::<core::integer::u8>",
        "members": [
          {
            "name": "snapshot",
            "type": "@core::array::Array::<core::integer::u8>"
          }
        ]
      },
      {
        "type": "enum",
        "name": "core::bool",
        "variants": [
          {
            "name": "False",
            "type": "()"
          },
          {
            "name": "True",
            "type": "()"
          }
        ]
      },
      {
        "type": "interface",
        "name": "dojo::world::IWorld",
        "items": [
          {
            "type": "function",
            "name": "metadata",
            "inputs": [
              {
                "name": "resource_id",
                "type": "core::felt252"
              }
            ],
            "outputs": [
              {
                "type": "dojo::resource_metadata::ResourceMetadata"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "set_metadata",
            "inputs": [
              {
                "name": "metadata",
                "type": "dojo::resource_metadata::ResourceMetadata"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "model",
            "inputs": [
              {
                "name": "name",
                "type": "core::felt252"
              }
            ],
            "outputs": [
              {
                "type": "(core::starknet::class_hash::ClassHash, core::starknet::contract_address::ContractAddress)"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "register_model",
            "inputs": [
              {
                "name": "class_hash",
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "deploy_contract",
            "inputs": [
              {
                "name": "salt",
                "type": "core::felt252"
              },
              {
                "name": "class_hash",
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "outputs": [
              {
                "type": "core::starknet::contract_address::ContractAddress"
              }
            ],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "upgrade_contract",
            "inputs": [
              {
                "name": "address",
                "type": "core::starknet::contract_address::ContractAddress"
              },
              {
                "name": "class_hash",
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "outputs": [
              {
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "uuid",
            "inputs": [],
            "outputs": [
              {
                "type": "core::integer::u32"
              }
            ],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "emit",
            "inputs": [
              {
                "name": "keys",
                "type": "core::array::Array::<core::felt252>"
              },
              {
                "name": "values",
                "type": "core::array::Span::<core::felt252>"
              }
            ],
            "outputs": [],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "entity",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "keys",
                "type": "core::array::Span::<core::felt252>"
              },
              {
                "name": "layout",
                "type": "core::array::Span::<core::integer::u8>"
              }
            ],
            "outputs": [
              {
                "type": "core::array::Span::<core::felt252>"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "set_entity",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "keys",
                "type": "core::array::Span::<core::felt252>"
              },
              {
                "name": "values",
                "type": "core::array::Span::<core::felt252>"
              },
              {
                "name": "layout",
                "type": "core::array::Span::<core::integer::u8>"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "base",
            "inputs": [],
            "outputs": [
              {
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "delete_entity",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "keys",
                "type": "core::array::Span::<core::felt252>"
              },
              {
                "name": "layout",
                "type": "core::array::Span::<core::integer::u8>"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "is_owner",
            "inputs": [
              {
                "name": "address",
                "type": "core::starknet::contract_address::ContractAddress"
              },
              {
                "name": "resource",
                "type": "core::felt252"
              }
            ],
            "outputs": [
              {
                "type": "core::bool"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "grant_owner",
            "inputs": [
              {
                "name": "address",
                "type": "core::starknet::contract_address::ContractAddress"
              },
              {
                "name": "resource",
                "type": "core::felt252"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "revoke_owner",
            "inputs": [
              {
                "name": "address",
                "type": "core::starknet::contract_address::ContractAddress"
              },
              {
                "name": "resource",
                "type": "core::felt252"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "is_writer",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "system",
                "type": "core::starknet::contract_address::ContractAddress"
              }
            ],
            "outputs": [
              {
                "type": "core::bool"
              }
            ],
            "state_mutability": "view"
          },
          {
            "type": "function",
            "name": "grant_writer",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "system",
                "type": "core::starknet::contract_address::ContractAddress"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          },
          {
            "type": "function",
            "name": "revoke_writer",
            "inputs": [
              {
                "name": "model",
                "type": "core::felt252"
              },
              {
                "name": "system",
                "type": "core::starknet::contract_address::ContractAddress"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          }
        ]
      },
      {
        "type": "impl",
        "name": "UpgradeableWorld",
        "interface_name": "dojo::world::IUpgradeableWorld"
      },
      {
        "type": "interface",
        "name": "dojo::world::IUpgradeableWorld",
        "items": [
          {
            "type": "function",
            "name": "upgrade",
            "inputs": [
              {
                "name": "new_class_hash",
                "type": "core::starknet::class_hash::ClassHash"
              }
            ],
            "outputs": [],
            "state_mutability": "external"
          }
        ]
      },
      {
        "type": "constructor",
        "name": "constructor",
        "inputs": [
          {
            "name": "contract_base",
            "type": "core::starknet::class_hash::ClassHash"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::WorldSpawned",
        "kind": "struct",
        "members": [
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          },
          {
            "name": "creator",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::ContractDeployed",
        "kind": "struct",
        "members": [
          {
            "name": "salt",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          },
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::ContractUpgraded",
        "kind": "struct",
        "members": [
          {
            "name": "class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          },
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::WorldUpgraded",
        "kind": "struct",
        "members": [
          {
            "name": "class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::MetadataUpdate",
        "kind": "struct",
        "members": [
          {
            "name": "resource",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "uri",
            "type": "core::array::Span::<core::felt252>",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::ModelRegistered",
        "kind": "struct",
        "members": [
          {
            "name": "name",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          },
          {
            "name": "prev_class_hash",
            "type": "core::starknet::class_hash::ClassHash",
            "kind": "data"
          },
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          },
          {
            "name": "prev_address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::StoreSetRecord",
        "kind": "struct",
        "members": [
          {
            "name": "table",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "keys",
            "type": "core::array::Span::<core::felt252>",
            "kind": "data"
          },
          {
            "name": "values",
            "type": "core::array::Span::<core::felt252>",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::StoreDelRecord",
        "kind": "struct",
        "members": [
          {
            "name": "table",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "keys",
            "type": "core::array::Span::<core::felt252>",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::WriterUpdated",
        "kind": "struct",
        "members": [
          {
            "name": "model",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "system",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          },
          {
            "name": "value",
            "type": "core::bool",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::OwnerUpdated",
        "kind": "struct",
        "members": [
          {
            "name": "address",
            "type": "core::starknet::contract_address::ContractAddress",
            "kind": "data"
          },
          {
            "name": "resource",
            "type": "core::felt252",
            "kind": "data"
          },
          {
            "name": "value",
            "type": "core::bool",
            "kind": "data"
          }
        ]
      },
      {
        "type": "event",
        "name": "dojo::world::world::Event",
        "kind": "enum",
        "variants": [
          {
            "name": "WorldSpawned",
            "type": "dojo::world::world::WorldSpawned",
            "kind": "nested"
          },
          {
            "name": "ContractDeployed",
            "type": "dojo::world::world::ContractDeployed",
            "kind": "nested"
          },
          {
            "name": "ContractUpgraded",
            "type": "dojo::world::world::ContractUpgraded",
            "kind": "nested"
          },
          {
            "name": "WorldUpgraded",
            "type": "dojo::world::world::WorldUpgraded",
            "kind": "nested"
          },
          {
            "name": "MetadataUpdate",
            "type": "dojo::world::world::MetadataUpdate",
            "kind": "nested"
          },
          {
            "name": "ModelRegistered",
            "type": "dojo::world::world::ModelRegistered",
            "kind": "nested"
          },
          {
            "name": "StoreSetRecord",
            "type": "dojo::world::world::StoreSetRecord",
            "kind": "nested"
          },
          {
            "name": "StoreDelRecord",
            "type": "dojo::world::world::StoreDelRecord",
            "kind": "nested"
          },
          {
            "name": "WriterUpdated",
            "type": "dojo::world::world::WriterUpdated",
            "kind": "nested"
          },
          {
            "name": "OwnerUpdated",
            "type": "dojo::world::world::OwnerUpdated",
            "kind": "nested"
          }
        ]
      }
    ],
    "address": "0x3a0394af68d1727a0019949a94fa584e8bc132903d49bb545888eb1bd427cf4",
    "transaction_hash": "0xa40e4cad10c4a8e31f0148f6ffb1dba7d5f668e86cb2af8d8c93a3e7a602b7",
    "block_number": 3,
    "seed": "blob_arena",
    "name": "dojo::world::world"
  },
  "base": {
    "kind": "Class",
    "class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
    "original_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
    "abi": null,
    "name": "dojo::base::base"
  },
  "contracts": [
    {
      "kind": "DojoContract",
      "address": "0x3e2408ea9affd43d731fcb31e67f7c2c6899cef4c1279dc597dc5d14b240d12",
      "class_hash": "0x5811732bc8864da296814301e254ea6c6b15c5553ea236a60f9111f137af3fe",
      "original_class_hash": "0x5811732bc8864da296814301e254ea6c6b15c5553ea236a60f9111f137af3fe",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "BlobertActionsImpl",
          "interface_name": "blob_arena::contracts::blobert::IBlobertActions"
        },
        {
          "type": "interface",
          "name": "blob_arena::contracts::blobert::IBlobertActions",
          "items": [
            {
              "type": "function",
              "name": "mint",
              "inputs": [
                {
                  "name": "owner",
                  "type": "core::starknet::contract_address::ContractAddress"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u128"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::contracts::blobert::blobert_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "blob_arena::contracts::blobert::blobert_actions"
    },
    {
      "kind": "DojoContract",
      "address": "0x3ce2e701b020ba2c2af15b7347c9d05a5f28b7060609295c6f461af326bc68c",
      "class_hash": "0x68982a375742204d392111f2949da6ad6c46d3c5db7fc22bc6b4dd024482675",
      "original_class_hash": "0x68982a375742204d392111f2949da6ad6c46d3c5db7fc22bc6b4dd024482675",
      "base_class_hash": "0x679177a2cb757694ac4f326d01052ff0963eac0bc2a17116a2b87badcdf6f76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoResourceProviderImpl",
          "interface_name": "dojo::world::IDojoResourceProvider"
        },
        {
          "type": "interface",
          "name": "dojo::world::IDojoResourceProvider",
          "items": [
            {
              "type": "function",
              "name": "dojo_resource",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "WorldProviderImpl",
          "interface_name": "dojo::world::IWorldProvider"
        },
        {
          "type": "struct",
          "name": "dojo::world::IWorldDispatcher",
          "members": [
            {
              "name": "contract_address",
              "type": "core::starknet::contract_address::ContractAddress"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::world::IWorldProvider",
          "items": [
            {
              "type": "function",
              "name": "world",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::world::IWorldDispatcher"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "ChallengeActionsImpl",
          "interface_name": "blob_arena::contracts::challenge::IChallengeActions"
        },
        {
          "type": "enum",
          "name": "blob_arena::components::combat::Move",
          "variants": [
            {
              "name": "Beat",
              "type": "()"
            },
            {
              "name": "Counter",
              "type": "()"
            },
            {
              "name": "Rush",
              "type": "()"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::contracts::challenge::IChallengeActions",
          "items": [
            {
              "type": "function",
              "name": "send_invite",
              "inputs": [
                {
                  "name": "receiver",
                  "type": "core::starknet::contract_address::ContractAddress"
                },
                {
                  "name": "blobert_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u128"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "rescind_invite",
              "inputs": [
                {
                  "name": "challenge_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "respond_invite",
              "inputs": [
                {
                  "name": "challenge_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "blobert_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "rescind_response",
              "inputs": [
                {
                  "name": "challenge_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "reject_invite",
              "inputs": [
                {
                  "name": "challenge_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "reject_response",
              "inputs": [
                {
                  "name": "challenge_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "accept_response",
              "inputs": [
                {
                  "name": "challenge_id",
                  "type": "core::integer::u128"
                }
              ],
              "outputs": [
                {
                  "type": "core::integer::u128"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "commit_move",
              "inputs": [
                {
                  "name": "challenge_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "hash",
                  "type": "core::felt252"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "reveal_move",
              "inputs": [
                {
                  "name": "challenge_id",
                  "type": "core::integer::u128"
                },
                {
                  "name": "move",
                  "type": "blob_arena::components::combat::Move"
                },
                {
                  "name": "salt",
                  "type": "core::felt252"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "UpgradableImpl",
          "interface_name": "dojo::components::upgradeable::IUpgradeable"
        },
        {
          "type": "interface",
          "name": "dojo::components::upgradeable::IUpgradeable",
          "items": [
            {
              "type": "function",
              "name": "upgrade",
              "inputs": [
                {
                  "name": "new_class_hash",
                  "type": "core::starknet::class_hash::ClassHash"
                }
              ],
              "outputs": [],
              "state_mutability": "external"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Upgraded",
          "kind": "struct",
          "members": [
            {
              "name": "class_hash",
              "type": "core::starknet::class_hash::ClassHash",
              "kind": "data"
            }
          ]
        },
        {
          "type": "event",
          "name": "dojo::components::upgradeable::upgradeable::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "Upgraded",
              "type": "dojo::components::upgradeable::upgradeable::Upgraded",
              "kind": "nested"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::contracts::challenge::challenge_actions::Event",
          "kind": "enum",
          "variants": [
            {
              "name": "UpgradeableEvent",
              "type": "dojo::components::upgradeable::upgradeable::Event",
              "kind": "nested"
            }
          ]
        }
      ],
      "reads": [],
      "writes": [],
      "computed": [],
      "name": "blob_arena::contracts::challenge::challenge_actions"
    }
  ],
  "models": [
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "id",
          "type": "u128",
          "key": true
        },
        {
          "name": "owner",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "traits",
          "type": "Traits",
          "key": false
        },
        {
          "name": "stats",
          "type": "Stats",
          "key": false
        }
      ],
      "class_hash": "0x36b5fa0a6ef4ee75ad46afe1468a259870432c08184ea86e29f02199b02141a",
      "original_class_hash": "0x36b5fa0a6ef4ee75ad46afe1468a259870432c08184ea86e29f02199b02141a",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "blobertImpl",
          "interface_name": "blob_arena::components::blobert::Iblobert"
        },
        {
          "type": "enum",
          "name": "blob_arena::components::background::Background",
          "variants": [
            {
              "name": "AvnuBlue",
              "type": "()"
            },
            {
              "name": "Blue",
              "type": "()"
            },
            {
              "name": "CryptsAndCaverns",
              "type": "()"
            },
            {
              "name": "FibrousFrame",
              "type": "()"
            },
            {
              "name": "Green",
              "type": "()"
            },
            {
              "name": "Holo",
              "type": "()"
            },
            {
              "name": "Orange",
              "type": "()"
            },
            {
              "name": "Purple",
              "type": "()"
            },
            {
              "name": "RealmsDark",
              "type": "()"
            },
            {
              "name": "Realms",
              "type": "()"
            },
            {
              "name": "Terraforms",
              "type": "()"
            },
            {
              "name": "Tulip",
              "type": "()"
            }
          ]
        },
        {
          "type": "enum",
          "name": "blob_arena::components::armour::Armour",
          "variants": [
            {
              "name": "SheepsWool",
              "type": "()"
            },
            {
              "name": "Kigurumi",
              "type": "()"
            },
            {
              "name": "DivineRobeDark",
              "type": "()"
            },
            {
              "name": "DivineRobe",
              "type": "()"
            },
            {
              "name": "DojoRobe",
              "type": "()"
            },
            {
              "name": "HolyChestplate",
              "type": "()"
            },
            {
              "name": "DemonHusk",
              "type": "()"
            },
            {
              "name": "LeatherArmour",
              "type": "()"
            },
            {
              "name": "LeopardSkin",
              "type": "()"
            },
            {
              "name": "LinenRobe",
              "type": "()"
            },
            {
              "name": "LordsArmor",
              "type": "()"
            },
            {
              "name": "SecretTattoo",
              "type": "()"
            },
            {
              "name": "Chainmail",
              "type": "()"
            },
            {
              "name": "Suit",
              "type": "()"
            },
            {
              "name": "Underpants",
              "type": "()"
            },
            {
              "name": "WenShirt",
              "type": "()"
            },
            {
              "name": "WsbTankTop",
              "type": "()"
            }
          ]
        },
        {
          "type": "enum",
          "name": "blob_arena::components::mask::Mask",
          "variants": [
            {
              "name": "Blobert",
              "type": "()"
            },
            {
              "name": "Doge",
              "type": "()"
            },
            {
              "name": "Dojo",
              "type": "()"
            },
            {
              "name": "Ducks",
              "type": "()"
            },
            {
              "name": "Kevin",
              "type": "()"
            },
            {
              "name": "Milady",
              "type": "()"
            },
            {
              "name": "Pepe",
              "type": "()"
            },
            {
              "name": "Pudgy",
              "type": "()"
            },
            {
              "name": "_3dGlasses",
              "type": "()"
            },
            {
              "name": "_1337Skulls",
              "type": "()"
            },
            {
              "name": "AncientHelm",
              "type": "()"
            },
            {
              "name": "Bane",
              "type": "()"
            },
            {
              "name": "BraavosHelm",
              "type": "()"
            },
            {
              "name": "Bulbhead",
              "type": "()"
            },
            {
              "name": "DealWithItGlasses",
              "type": "()"
            },
            {
              "name": "DemonCrown",
              "type": "()"
            },
            {
              "name": "DivineHood",
              "type": "()"
            },
            {
              "name": "Ekubo",
              "type": "()"
            },
            {
              "name": "HyperlootCrown",
              "type": "()"
            },
            {
              "name": "InfluenceHelmet",
              "type": "()"
            },
            {
              "name": "LordsHelm",
              "type": "()"
            },
            {
              "name": "Nostrahat",
              "type": "()"
            },
            {
              "name": "NounsGlasses",
              "type": "()"
            },
            {
              "name": "PopeHat",
              "type": "()"
            },
            {
              "name": "TaprootWizardHat",
              "type": "()"
            },
            {
              "name": "WifHat",
              "type": "()"
            }
          ]
        },
        {
          "type": "enum",
          "name": "blob_arena::components::jewelry::Jewelry",
          "variants": [
            {
              "name": "Amulet",
              "type": "()"
            },
            {
              "name": "BronzeRing",
              "type": "()"
            },
            {
              "name": "GoldRing",
              "type": "()"
            },
            {
              "name": "Necklace",
              "type": "()"
            },
            {
              "name": "Pendant",
              "type": "()"
            },
            {
              "name": "PlatinumRing",
              "type": "()"
            },
            {
              "name": "SilverRing",
              "type": "()"
            },
            {
              "name": "TitaniumRing",
              "type": "()"
            }
          ]
        },
        {
          "type": "enum",
          "name": "blob_arena::components::weapon::Weapon",
          "variants": [
            {
              "name": "AlgorithmicAegis",
              "type": "()"
            },
            {
              "name": "ArgentShield",
              "type": "()"
            },
            {
              "name": "Balloons",
              "type": "()"
            },
            {
              "name": "BannerOfAnger",
              "type": "()"
            },
            {
              "name": "BannerOfBrilliance",
              "type": "()"
            },
            {
              "name": "BannerOfDetection",
              "type": "()"
            },
            {
              "name": "BannerOfEnlightenment",
              "type": "()"
            },
            {
              "name": "BannerOfFury",
              "type": "()"
            },
            {
              "name": "BannerOfGiants",
              "type": "()"
            },
            {
              "name": "BannerOfPerfection",
              "type": "()"
            },
            {
              "name": "BannerOfPower",
              "type": "()"
            },
            {
              "name": "BannerOfProtection",
              "type": "()"
            },
            {
              "name": "BannerOfRage",
              "type": "()"
            },
            {
              "name": "BannerOfReflection",
              "type": "()"
            },
            {
              "name": "BannerOfSkill",
              "type": "()"
            },
            {
              "name": "BannerOfTheFox",
              "type": "()"
            },
            {
              "name": "BannerOfTheTwins",
              "type": "()"
            },
            {
              "name": "BannerOfTitans",
              "type": "()"
            },
            {
              "name": "BannerOfTonyHawk",
              "type": "()"
            },
            {
              "name": "BannerOfVitriol",
              "type": "()"
            },
            {
              "name": "Banner",
              "type": "()"
            },
            {
              "name": "Briq",
              "type": "()"
            },
            {
              "name": "Calculator",
              "type": "()"
            },
            {
              "name": "DevvingForTheDistracted",
              "type": "()"
            },
            {
              "name": "DiamondHands",
              "type": "()"
            },
            {
              "name": "DopeUzi",
              "type": "()"
            },
            {
              "name": "GhostWand",
              "type": "()"
            },
            {
              "name": "Grimoire",
              "type": "()"
            },
            {
              "name": "GrugsClub",
              "type": "()"
            },
            {
              "name": "JediswapSaber",
              "type": "()"
            },
            {
              "name": "Katana",
              "type": "()"
            },
            {
              "name": "LordsBanner",
              "type": "()"
            },
            {
              "name": "LsHasNoChill",
              "type": "()"
            },
            {
              "name": "Mandolin",
              "type": "()"
            },
            {
              "name": "SignIso",
              "type": "()"
            },
            {
              "name": "SignatureBanner",
              "type": "()"
            },
            {
              "name": "SithswapSaber",
              "type": "()"
            },
            {
              "name": "Spaghetti",
              "type": "()"
            },
            {
              "name": "Squid",
              "type": "()"
            },
            {
              "name": "StarkMagic",
              "type": "()"
            },
            {
              "name": "StarkShield",
              "type": "()"
            },
            {
              "name": "Stool",
              "type": "()"
            },
            {
              "name": "Warhammer",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "blob_arena::components::blobert::Traits",
          "members": [
            {
              "name": "background",
              "type": "blob_arena::components::background::Background"
            },
            {
              "name": "armour",
              "type": "blob_arena::components::armour::Armour"
            },
            {
              "name": "mask",
              "type": "blob_arena::components::mask::Mask"
            },
            {
              "name": "jewelry",
              "type": "blob_arena::components::jewelry::Jewelry"
            },
            {
              "name": "weapon",
              "type": "blob_arena::components::weapon::Weapon"
            }
          ]
        },
        {
          "type": "struct",
          "name": "blob_arena::components::stats::Stats",
          "members": [
            {
              "name": "attack",
              "type": "core::integer::u8"
            },
            {
              "name": "defense",
              "type": "core::integer::u8"
            },
            {
              "name": "speed",
              "type": "core::integer::u8"
            },
            {
              "name": "strength",
              "type": "core::integer::u8"
            }
          ]
        },
        {
          "type": "struct",
          "name": "blob_arena::components::blobert::Blobert",
          "members": [
            {
              "name": "id",
              "type": "core::integer::u128"
            },
            {
              "name": "owner",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "traits",
              "type": "blob_arena::components::blobert::Traits"
            },
            {
              "name": "stats",
              "type": "blob_arena::components::stats::Stats"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::blobert::Iblobert",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::blobert::Blobert"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::blobert::blobert::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::blobert::blobert"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "challenge_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "sender",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "receiver",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "blobert_id",
          "type": "u128",
          "key": false
        },
        {
          "name": "open",
          "type": "bool",
          "key": false
        }
      ],
      "class_hash": "0x3ec83d9ead7c824ebd8606076783b120ea821ca0475f16b538b4dddda880a6c",
      "original_class_hash": "0x3ec83d9ead7c824ebd8606076783b120ea821ca0475f16b538b4dddda880a6c",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "challenge_inviteImpl",
          "interface_name": "blob_arena::components::challenge::Ichallenge_invite"
        },
        {
          "type": "enum",
          "name": "core::bool",
          "variants": [
            {
              "name": "False",
              "type": "()"
            },
            {
              "name": "True",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "blob_arena::components::challenge::ChallengeInvite",
          "members": [
            {
              "name": "challenge_id",
              "type": "core::integer::u128"
            },
            {
              "name": "sender",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "receiver",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "blobert_id",
              "type": "core::integer::u128"
            },
            {
              "name": "open",
              "type": "core::bool"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::challenge::Ichallenge_invite",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::challenge::ChallengeInvite"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::challenge::challenge_invite::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::challenge::challenge_invite"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "challenge_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "blobert_id",
          "type": "u128",
          "key": false
        },
        {
          "name": "open",
          "type": "bool",
          "key": false
        },
        {
          "name": "combat_id",
          "type": "u128",
          "key": false
        }
      ],
      "class_hash": "0x5325038ef3ad607a64e9ba74d3be798ef9f53e6ea49a25cde831580e18c1e83",
      "original_class_hash": "0x5325038ef3ad607a64e9ba74d3be798ef9f53e6ea49a25cde831580e18c1e83",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "challenge_responseImpl",
          "interface_name": "blob_arena::components::challenge::Ichallenge_response"
        },
        {
          "type": "enum",
          "name": "core::bool",
          "variants": [
            {
              "name": "False",
              "type": "()"
            },
            {
              "name": "True",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "blob_arena::components::challenge::ChallengeResponse",
          "members": [
            {
              "name": "challenge_id",
              "type": "core::integer::u128"
            },
            {
              "name": "blobert_id",
              "type": "core::integer::u128"
            },
            {
              "name": "open",
              "type": "core::bool"
            },
            {
              "name": "combat_id",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::challenge::Ichallenge_response",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::challenge::ChallengeResponse"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::challenge::challenge_response::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::challenge::challenge_response"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "player",
          "type": "ContractAddress",
          "key": true
        },
        {
          "name": "blobert_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "wins",
          "type": "u64",
          "key": false
        },
        {
          "name": "losses",
          "type": "u64",
          "key": false
        },
        {
          "name": "max_consecutive_wins",
          "type": "u64",
          "key": false
        },
        {
          "name": "current_consecutive_wins",
          "type": "u64",
          "key": false
        }
      ],
      "class_hash": "0x179527eeab9943803320276ed8ff5efdebdb6aeb3497c4a0b05c77fb3bf5c76",
      "original_class_hash": "0x179527eeab9943803320276ed8ff5efdebdb6aeb3497c4a0b05c77fb3bf5c76",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "challenge_scoreImpl",
          "interface_name": "blob_arena::components::challenge::Ichallenge_score"
        },
        {
          "type": "struct",
          "name": "blob_arena::components::challenge::ChallengeScore",
          "members": [
            {
              "name": "player",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "blobert_id",
              "type": "core::integer::u128"
            },
            {
              "name": "wins",
              "type": "core::integer::u64"
            },
            {
              "name": "losses",
              "type": "core::integer::u64"
            },
            {
              "name": "max_consecutive_wins",
              "type": "core::integer::u64"
            },
            {
              "name": "current_consecutive_wins",
              "type": "core::integer::u64"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::challenge::Ichallenge_score",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::challenge::ChallengeScore"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::challenge::challenge_score::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::challenge::challenge_score"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "id",
          "type": "u128",
          "key": true
        },
        {
          "name": "a",
          "type": "felt252",
          "key": false
        },
        {
          "name": "b",
          "type": "felt252",
          "key": false
        }
      ],
      "class_hash": "0x5402627c69510b384cef751ad3f6b2f6986032edcfce1332d771f748f6270c1",
      "original_class_hash": "0x5402627c69510b384cef751ad3f6b2f6986032edcfce1332d771f748f6270c1",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "two_hashesImpl",
          "interface_name": "blob_arena::components::combat::Itwo_hashes"
        },
        {
          "type": "struct",
          "name": "blob_arena::components::combat::TwoHashes",
          "members": [
            {
              "name": "id",
              "type": "core::integer::u128"
            },
            {
              "name": "a",
              "type": "core::felt252"
            },
            {
              "name": "b",
              "type": "core::felt252"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::combat::Itwo_hashes",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::combat::TwoHashes"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::combat::two_hashes::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::combat::two_hashes"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "id",
          "type": "u128",
          "key": true
        },
        {
          "name": "a",
          "type": "MoveN",
          "key": false
        },
        {
          "name": "b",
          "type": "MoveN",
          "key": false
        }
      ],
      "class_hash": "0x6e20a07aeda0c06d1f0bfd6b17e10d2890b169d22f8723f0a1d20c12bbcf563",
      "original_class_hash": "0x6e20a07aeda0c06d1f0bfd6b17e10d2890b169d22f8723f0a1d20c12bbcf563",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "two_movesImpl",
          "interface_name": "blob_arena::components::combat::Itwo_moves"
        },
        {
          "type": "enum",
          "name": "blob_arena::components::combat::MoveN",
          "variants": [
            {
              "name": "None",
              "type": "()"
            },
            {
              "name": "Beat",
              "type": "()"
            },
            {
              "name": "Counter",
              "type": "()"
            },
            {
              "name": "Rush",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "blob_arena::components::combat::TwoMoves",
          "members": [
            {
              "name": "id",
              "type": "core::integer::u128"
            },
            {
              "name": "a",
              "type": "blob_arena::components::combat::MoveN"
            },
            {
              "name": "b",
              "type": "blob_arena::components::combat::MoveN"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::combat::Itwo_moves",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::combat::TwoMoves"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::combat::two_moves::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::combat::two_moves"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "combat_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "a",
          "type": "u8",
          "key": false
        },
        {
          "name": "b",
          "type": "u8",
          "key": false
        }
      ],
      "class_hash": "0x1653ef83291f39de25123ed955b35a54599b130c5d109c9c27ca7f03964ae6e",
      "original_class_hash": "0x1653ef83291f39de25123ed955b35a54599b130c5d109c9c27ca7f03964ae6e",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "healthsImpl",
          "interface_name": "blob_arena::components::knockout::Ihealths"
        },
        {
          "type": "struct",
          "name": "blob_arena::components::knockout::Healths",
          "members": [
            {
              "name": "combat_id",
              "type": "core::integer::u128"
            },
            {
              "name": "a",
              "type": "core::integer::u8"
            },
            {
              "name": "b",
              "type": "core::integer::u8"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::knockout::Ihealths",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::knockout::Healths"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::knockout::healths::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::knockout::healths"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "combat_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "player_a",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "player_b",
          "type": "ContractAddress",
          "key": false
        },
        {
          "name": "blobert_a",
          "type": "u128",
          "key": false
        },
        {
          "name": "blobert_b",
          "type": "u128",
          "key": false
        }
      ],
      "class_hash": "0x2d7ac463d6571c181105e6e5671e0510dfee7bdddc948cf4a8607858a5e5e42",
      "original_class_hash": "0x2d7ac463d6571c181105e6e5671e0510dfee7bdddc948cf4a8607858a5e5e42",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "knockoutImpl",
          "interface_name": "blob_arena::components::knockout::Iknockout"
        },
        {
          "type": "struct",
          "name": "blob_arena::components::knockout::Knockout",
          "members": [
            {
              "name": "combat_id",
              "type": "core::integer::u128"
            },
            {
              "name": "player_a",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "player_b",
              "type": "core::starknet::contract_address::ContractAddress"
            },
            {
              "name": "blobert_a",
              "type": "core::integer::u128"
            },
            {
              "name": "blobert_b",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::knockout::Iknockout",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::knockout::Knockout"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::knockout::knockout::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::knockout::knockout"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "combat_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "health_a",
          "type": "u8",
          "key": false
        },
        {
          "name": "health_b",
          "type": "u8",
          "key": false
        },
        {
          "name": "move_a",
          "type": "Move",
          "key": false
        },
        {
          "name": "move_b",
          "type": "Move",
          "key": false
        },
        {
          "name": "damage_a",
          "type": "u8",
          "key": false
        },
        {
          "name": "damage_b",
          "type": "u8",
          "key": false
        }
      ],
      "class_hash": "0x35d18beead74620a4a3d7222da744b0f4694ba5320b113c82ce24c7a81bfdc",
      "original_class_hash": "0x35d18beead74620a4a3d7222da744b0f4694ba5320b113c82ce24c7a81bfdc",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "last_roundImpl",
          "interface_name": "blob_arena::components::knockout::Ilast_round"
        },
        {
          "type": "enum",
          "name": "blob_arena::components::combat::Move",
          "variants": [
            {
              "name": "Beat",
              "type": "()"
            },
            {
              "name": "Counter",
              "type": "()"
            },
            {
              "name": "Rush",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "blob_arena::components::knockout::LastRound",
          "members": [
            {
              "name": "combat_id",
              "type": "core::integer::u128"
            },
            {
              "name": "health_a",
              "type": "core::integer::u8"
            },
            {
              "name": "health_b",
              "type": "core::integer::u8"
            },
            {
              "name": "move_a",
              "type": "blob_arena::components::combat::Move"
            },
            {
              "name": "move_b",
              "type": "blob_arena::components::combat::Move"
            },
            {
              "name": "damage_a",
              "type": "core::integer::u8"
            },
            {
              "name": "damage_b",
              "type": "core::integer::u8"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::knockout::Ilast_round",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::knockout::LastRound"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::knockout::last_round::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::knockout::last_round"
    },
    {
      "kind": "DojoModel",
      "members": [
        {
          "name": "combat_id",
          "type": "u128",
          "key": true
        },
        {
          "name": "amount",
          "type": "u256",
          "key": false
        },
        {
          "name": "blobert",
          "type": "bool",
          "key": false
        }
      ],
      "class_hash": "0x53253a3b528d02a6c01e639cc798bfed2190fca48342a55d45c8f3572001e00",
      "original_class_hash": "0x53253a3b528d02a6c01e639cc798bfed2190fca48342a55d45c8f3572001e00",
      "abi": [
        {
          "type": "impl",
          "name": "DojoModelImpl",
          "interface_name": "dojo::model::IDojoModel"
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::integer::u8>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::integer::u8>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::felt252>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::felt252>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<core::array::Span::<core::felt252>>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Struct",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>",
          "members": [
            {
              "name": "snapshot",
              "type": "@core::array::Array::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "struct",
          "name": "dojo::database::introspect::Enum",
          "members": [
            {
              "name": "name",
              "type": "core::felt252"
            },
            {
              "name": "attrs",
              "type": "core::array::Span::<core::felt252>"
            },
            {
              "name": "children",
              "type": "core::array::Span::<(core::felt252, core::array::Span::<core::felt252>)>"
            }
          ]
        },
        {
          "type": "enum",
          "name": "dojo::database::introspect::Ty",
          "variants": [
            {
              "name": "Primitive",
              "type": "core::felt252"
            },
            {
              "name": "Struct",
              "type": "dojo::database::introspect::Struct"
            },
            {
              "name": "Enum",
              "type": "dojo::database::introspect::Enum"
            },
            {
              "name": "Tuple",
              "type": "core::array::Span::<core::array::Span::<core::felt252>>"
            },
            {
              "name": "Array",
              "type": "core::integer::u32"
            }
          ]
        },
        {
          "type": "interface",
          "name": "dojo::model::IDojoModel",
          "items": [
            {
              "type": "function",
              "name": "name",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::felt252"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "unpacked_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "packed_size",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::integer::u32"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "layout",
              "inputs": [],
              "outputs": [
                {
                  "type": "core::array::Span::<core::integer::u8>"
                }
              ],
              "state_mutability": "view"
            },
            {
              "type": "function",
              "name": "schema",
              "inputs": [],
              "outputs": [
                {
                  "type": "dojo::database::introspect::Ty"
                }
              ],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "impl",
          "name": "stakeImpl",
          "interface_name": "blob_arena::components::stake::Istake"
        },
        {
          "type": "struct",
          "name": "core::integer::u256",
          "members": [
            {
              "name": "low",
              "type": "core::integer::u128"
            },
            {
              "name": "high",
              "type": "core::integer::u128"
            }
          ]
        },
        {
          "type": "enum",
          "name": "core::bool",
          "variants": [
            {
              "name": "False",
              "type": "()"
            },
            {
              "name": "True",
              "type": "()"
            }
          ]
        },
        {
          "type": "struct",
          "name": "blob_arena::components::stake::Stake",
          "members": [
            {
              "name": "combat_id",
              "type": "core::integer::u128"
            },
            {
              "name": "amount",
              "type": "core::integer::u256"
            },
            {
              "name": "blobert",
              "type": "core::bool"
            }
          ]
        },
        {
          "type": "interface",
          "name": "blob_arena::components::stake::Istake",
          "items": [
            {
              "type": "function",
              "name": "ensure_abi",
              "inputs": [
                {
                  "name": "model",
                  "type": "blob_arena::components::stake::Stake"
                }
              ],
              "outputs": [],
              "state_mutability": "view"
            }
          ]
        },
        {
          "type": "event",
          "name": "blob_arena::components::stake::stake::Event",
          "kind": "enum",
          "variants": []
        }
      ],
      "name": "blob_arena::components::stake::stake"
    }
  ]
}
"""

MANIFEST = MANIFEST_BA

project_name = ""
repo_name = ""

type_mapping = {
    "u8": "byte",
    "bool": "bool",
    "u16": "UInt16",
    "u32": "UInt32",
    "u64": "UInt64",
    "u128": "FieldElement",
    "ContractAddress": "FieldElement",
    "felt252": "FieldElement"
}

classContractTemplate = Template("""
public static class ${className}Contract
{
    ${functionNames}
                           
    ${enums}       

    ${structs}

    ${methods}
}
""")

functionHalfTemplate = Template("""
        public static async Task<FieldElement> ${functionHeader} 
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                       ${dataStructInput}
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with ${functionName}" + ex.Message);
                return null;
            }
        }
""")

functionFullTemplate = Template("""
        public static async Task<FieldElement> ${functionHeader} 
        {
            if (selectedWalletType == WalletType.BURNER)
            {   
              try
              {
                  var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                  {
                  new dojo.Call
                  {
                      calldata = new dojo.FieldElement[]
                      {
                        ${dataStructInput}
                      },
                      selector = endpointData.functionName,
                      to = endpointData.addressOfSystem,
                  }
                  });

                  return transaction;
              }
              catch (Exception ex)
              {
                  Debug.Log("issue with ${functionName}" + ex.Message);
                  return null;
              }
            }
            else
            {
                ${inputsChain}

                string calldataString = JsonUtility.ToJson(new ArrayWrapper { array = arr });

                JSInteropManager.SendTransaction(endpointData.addressOfSystem, endpointData.functionName, calldataString, endpointData.objectName, endpointData.callbackFunctionName);

                return null;
            }
        }
""")

switchCaseTemplate = Template("""
        case FunctionNames.${functionNameInCs}:
            return "${functionNameInDojo}";\n
""")

functionNamesTemplate = Template(""" 
        public enum FunctionNames
        {
            ${enumFields}
        }
                                 
        public static string EnumToString(this FunctionNames functionName)
        {
            switch (functionName)
            {
                ${cases}
                default:
                    return "";
            }
        }
""")

modelFieldTemplate = Template("""
    [ModelField("${nameOfVarinDojo}")]
    public ${typeCs} dojo${modelNameInCs};
    \n
""")

modelScriptTemplate = Template("""
using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;

public class ${modelName} : ModelInstance
{                     
    #region GeneratedRegion                      
    ${allModels}
    #endregion
                              
    private void Start()
    {
        
    }
                               
    private void Update()
    {
        
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

    }
}
""")

enumTemplate = Template("""
        public enum ${enumName}
        {
            ${enumFields}
        }
""")

structTemplate = Template("""
        public struct ${structName}
        {
            ${structFields}
                          
            public ${structName}( ${structConstructorInputs} )
            {
                  ${structConstructorAssignments}
            }
        }
""")

 # add a constructor to all structs

        # public struct SendInviteStruct
        # {
        #     public FieldElement receiver;
        #     public FieldElement blobertId;

        #     public SendInviteStruct(FieldElement receiver, FieldElement blobertId)
        #     {
        #         this.receiver = receiver;
        #         this.blobertId = blobertId;
        #     }
        # }

dojoContractCommHalfTemplate = Template("""
using Dojo.Starknet;
using dojo_bindings;
using System;
using System.Threading.Tasks;
using UnityEngine;

namespace DojoContractCommunication
{
    public struct EndpointDojoCallStruct
    {
        public Account account;
        public string functionName;
        public string addressOfSystem;
    }
                                    
                                
    ${classes}
}
""")

dojoContractCommFullTemplate = Template("""
using Dojo.Starknet;
using dojo_bindings;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using UnityEngine;
using Utils;
using static JSInteropManager;

namespace DojoContractCommunication
{
    public enum WalletType
    {
        BURNER,
        ARGENT_X,
        BRAAVOS
    }

    public static WalletType selectedWalletType 
    { 
      get; 
      set; 
    }                  
    
    public struct EndpointDojoCallStruct
    {
        public Account account;
        public string functionName;
        public string addressOfSystem;
        public string objectName;
        public string callbackFunctionName;
    }
                                                  
    ${classes}
}
""")

utilsStaticTemplate = """
    public static string emptyFieldElement = "0x0000000000000000000000000000000000000000000000000000000000000000";

    [Serializable]
    public struct u256
    {
        public BigInteger high;
        public BigInteger low;
    }

    public static float HexToNumber(string hexString, int decimalPlace = 0)
    {
        hexString = hexString.StartsWith("0x", StringComparison.OrdinalIgnoreCase) ? hexString[2..] : hexString;

        BigInteger number = BigInteger.Parse(hexString, System.Globalization.NumberStyles.HexNumber);

        number /= BigInteger.Pow(10, 12);

        float result = (float)(int)number / 1000000f;   //10^6
         
        if (decimalPlace > 0 && 6 > decimalPlace)
        {
            result = (float)Math.Round(result, decimalPlace);
        }

        return result;
    }
"""

utilsScriptTemplate = Template("""
using Dojo.Starknet;
using System;
using System.Numerics;
using System.Runtime.InteropServices;

public static class ${nameOfProject}Utils
{
    #region GeneratedRegion       
                               
    ${utilsStatics}   
                                                       
    ${enums}
                               
    #endregion
}
""")


class Function:
    def __init__(self):
        self.nameOfFunction = ""
        self.inputs: List[Variable] = []

class Enum:
    def __init__(self):
        self.enumName = ""
        self.enumOptionsName = []

class Model:
    def __init__(self):
        self.nameOfModel = ""
        self.variablesInTheModel: List[Variable] = []
        self.fullCsScript = ""
        self.justModelSection = ""

    def GenerateModelScript(self):
        allModels = ""
        for variable in self.variablesInTheModel:
            field = modelFieldTemplate.substitute(
                nameOfVarinDojo=variable.nameOfvariableDojo,
                typeCs=variable.typeOfInputCs,
                modelNameInCs=header_name_format(variable.nameOfvariableDojo)
            )
            allModels += field

        self.justModelSection = allModels
        self.fullCsScript = modelScriptTemplate.substitute(
            modelName=header_name_format(self.nameOfModel),
            allModels=allModels
        )
        return self.fullCsScript

class Variable:
    def __init__(self, nameOfvariableDojo="", nameOfvariableCs="", typeOfInputDojo="", typeOfInputCs=""):
        self.nameOfvariableDojo = nameOfvariableDojo
        self.nameOfvariableCs = nameOfvariableCs
        self.typeOfInputDojo = typeOfInputDojo
        self.typeOfInputCs = typeOfInputCs

class System:
    def __init__(self):
        self.systemName = ""
        self.systemAddress = ""
        self.functionsInSystem: List[Function] = []
        self.enumsInSystem: List[Enum] = []

        self.cSharpFunctionSection = ""
        self.functionNameSection = ""
        self.structSection = ""
        self.enumSection = ""

    def generate_csharp_functions(self, full=False):
        for function in self.functionsInSystem:
            functionName = header_name_format(function.nameOfFunction)
            functionHeader = f"{functionName}Call({functionName}Struct dataStruct, EndpointDojoCallStruct endpointData)"
            dataStructInput = self.format_function_inputs(function)

            if full:
                litsOfInputs = ""
                for input in function.inputs:
                    if input.typeOfInputCs == "FieldElement" or input.typeOfInputCs == "u256":
                        litsOfInputs += f"dataStruct.{input.nameOfvariableCs}.Hex().ToString(), "
                    else:
                        litsOfInputs += f"dataStruct.{input.nameOfvariableCs}.ToString(), "

                onChainInputs = f"var arr = new string[{len(function.inputs)}] {{{litsOfInputs}}};"

                self.cSharpFunctionSection += functionFullTemplate.substitute(
                  functionHeader=functionHeader,
                  dataStructInput=dataStructInput,
                  functionName=functionName,
                  inputsChain=onChainInputs
                )
                pass
            else:
              self.cSharpFunctionSection += functionHalfTemplate.substitute(
                  functionHeader=functionHeader,
                  dataStructInput=dataStructInput,
                  functionName=functionName
              )
        return self.cSharpFunctionSection

    def format_function_inputs(self, function):
        inputs = ""
        for input in function.inputs:
            template = Template('new FieldElement(dataStruct.${varName}.ToString("X")).Inner,\n' if input.typeOfInputCs != "FieldElement" else 'dataStruct.${varName}.Inner,\n')
            inputs += template.substitute(varName=var_name_format(input.nameOfvariableDojo))
        return inputs

    def generate_function_names_enum(self):
        allNames, cases = "", ""
        for function in self.functionsInSystem:
            formattedName = header_name_format(function.nameOfFunction)
            allNames += f"{formattedName},\n"
            cases += switchCaseTemplate.substitute(
                functionNameInCs=formattedName,
                functionNameInDojo=function.nameOfFunction
            )

        self.functionNameSection = functionNamesTemplate.substitute(
            enumFields=allNames,
            cases=cases
        )
        return self.functionNameSection

    def generate_structs(self):
        for function in self.functionsInSystem:
            structName = header_name_format(function.nameOfFunction) + "Struct"
            structInputs = "".join(f"public {input.typeOfInputCs} {input.nameOfvariableCs};\n" for input in function.inputs)
            structConstructorInputs = ", ".join(f"{input.typeOfInputCs} {input.nameOfvariableCs}" for input in function.inputs)
            structConstructorAssignments = "".join(f"this.{input.nameOfvariableCs} = {input.nameOfvariableCs};\n" for input in function.inputs)

            self.structSection += structTemplate.substitute(
                structName=structName,
                structFields=structInputs,
                structConstructorInputs=structConstructorInputs,
                structConstructorAssignments=structConstructorAssignments
            )
        return self.structSection

    def generate_enums(self):
        for enum in self.enumsInSystem:
            enumFields = ",\n".join(enum.enumOptionsName)
            
            self.enumSection += enumTemplate.substitute(
                enumName=enum.enumName,
                enumFields=enumFields
            ) + "\n"
        return self.enumSection

class Struct:
    def __init__(self):
        self.structNameDojo = ""
        self.structNameCs = ""
        self.variables: List[Variable] = []


def header_name_format(input_string) -> str:
    return ''.join(x.capitalize() for x in input_string.split('_'))

def var_name_format(input_string) -> str:
    parts = input_string.split("_")
    capitalized_parts = [parts[0]] + [part.capitalize() for part in parts[1:]]
    return "".join(capitalized_parts)

def create_system(contract: dict, type_mapping: dict, project_name: str):
    """
    Creates a system object from a contract JSON structure.

    Args:
    contract (dict): Contract data including name, address, and ABI.
    type_mapping (dict): Mapping of Dojo types to C# types.
    
    Returns:
    System: An instance of System with parsed functions and enums.
    """
    system = System()
    system_name = contract["name"].rsplit("::", 1)[0]
    system.systemName = contract["name"].rsplit("::", 1)[1]
    system.systemAddress = contract["address"]

    for abi in contract["abi"]:
        if abi["type"] == "interface" and abi["name"].startswith(system_name):
            parse_interface_items(system, abi["items"], type_mapping, project_name)
        elif abi["type"] == "enum":
            parse_enum(system, abi)

    return system

def parse_interface_items(system: System, items: List[dict], type_mapping: dict, project_name: str):
    """
    Parses interface items from the ABI and updates the system functions.
    
    Args:
    system (System): The system object to update.
    items (List[dict]): Items from the ABI of the contract.
    type_mapping (dict): Mapping of Dojo types to C# types.
    """
    for item in items:
        if item["type"] == "function":
            function = Function()
            function.nameOfFunction = item["name"]
            function.inputs = [
                Variable(
                    nameOfvariableDojo=input["name"],
                    typeOfInputDojo=input["type"].rsplit("::", 1)[1],
                    nameOfvariableCs=var_name_format(input["name"]),
                    typeOfInputCs=type_mapping.get(input["type"].rsplit("::", 1)[1], f"{project_name}Utils.{input['type'].rsplit('::', 1)[1]}")
                )
                for input in item["inputs"]
            ]
            system.functionsInSystem.append(function)

def parse_enum(system: System, abi: dict):
    """
    Parses enum information from the ABI and updates the system enums.
    
    Args:
    system (System): The system object to update.
    abi (dict): ABI information for the enum.
    """
    enum = Enum()
    enum.enumName = abi["name"].rsplit("::", 1)[1]
    enum.enumOptionsName = [variant["name"] for variant in abi["variants"]]
    system.enumsInSystem.append(enum)

def create_file(filename: str, extension: str, content: str, folder: str):
    """
    Create or update a file with the given filename, extension, and content in the specified folder.
    
    Args:
    filename (str): The base name of the file.
    extension (str): The extension of the file, can be provided with or without a leading dot.
    content (str): The content to be written into the file.
    folder (str): The path to the folder where the file will be created.
    """
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder)
    os.makedirs(directory, exist_ok=True)
    full_path = os.path.join(directory, f"{filename}.{extension.lstrip('.')}")  # Ensure dot is managed correctly
    
    with open(full_path, 'w') as file:
        file.write(content)

    print(f"File '{full_path}' has been created in the directory '{directory}'.")

def update_or_create_script(filename: str, extension: str, whole_content: str , generated_content_only: str, folder: str):
    """
    Updates or creates a new model script in the specified folder with the provided model information.
    
    Args:
    filename (str): The base name of the file.
    extension (str): The extension of the file, can be provided with or without a leading dot.
    model (Model): The model object containing the necessary data.
    folder (str): The path to the folder where the file will be created.
    """
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder)
    os.makedirs(directory, exist_ok=True)
    full_path = os.path.join(directory, f"{filename}.{extension.lstrip('.')}")  # Ensure dot is managed correctly
    
    if os.path.exists(full_path):
        with open(full_path, 'r') as file:
            lines = file.readlines()

        start_index = next((i for i, line in enumerate(lines) if "#region GeneratedRegion" in line), None)
        end_index = next((i for i, line in enumerate(lines) if "#endregion" in line and start_index is not None), None)
        
        if start_index is not None and end_index is not None:
            updated_lines = lines[:start_index+1] + [generated_content_only] + lines[end_index:]
            with open(full_path, 'w') as file:
                file.writelines(updated_lines)
            print(f"Updated the GeneratedRegion section in '{full_path}'.")
        else:
            print(f"No region found in '{full_path}'. Creating new script.")
            with open(full_path, 'w') as file:
                file.write(whole_content)
    else:
        with open(full_path, 'w') as file:
            file.write(whole_content)
        print(f"Created new file '{full_path}'.")

def load_manifest(file_path: str):
    with open(file_path, 'r') as file:
        return json.load(file)

def create_systems(contract_data, project_name):
    systems = []
    for contract in contract_data:
        system = create_system(contract, type_mapping, project_name)
        systems.append(system)
    return systems

def generate_classes(systems: List[System], template, full=False):
    all_classes = ""
    for system in systems:
        print(system.systemName)
        print(system.systemAddress)
        system.generate_csharp_functions(full=full)
        system.generate_function_names_enum()
        system.generate_structs()

        all_classes += template.substitute(
            functionNames=system.functionNameSection, 
            structs=system.structSection,
            methods=system.cSharpFunctionSection,
            className=header_name_format(system.systemName),
            enums=""
        )
        # print("\n\n\n\n")
    return all_classes

def generate_full_script(template, classes):
    return template.substitute(classes=classes)

def parse_models(manifest_data, type_mapping,project_name, repo_name):
    allModels : List[Model]= []

    for models in manifest_data["models"]:
        newModel = Model()
        newModel.nameOfModel = models["name"].rsplit("::", 1)[1]
        newModel.variablesInTheModel = parse_variables(models["members"], type_mapping, project_name)
        allModels.append(newModel)
        newModel.GenerateModelScript()
        update_or_create_script(header_name_format(newModel.nameOfModel), "cs", newModel.fullCsScript, newModel.justModelSection, "Models")
    return allModels

def parse_variables(members, type_mapping,project_name ):
    variables = []
    for member in members:
        new_variable = Variable()
        new_variable.nameOfvariableDojo = member["name"]
        new_variable.nameOfvariableCs = var_name_format(member["name"])
        type_info = member["type"]
        new_variable.typeOfInputDojo = type_info
        if type_info in type_mapping:
            new_variable.typeOfInputCs = type_mapping[type_info]
        else:
            new_variable.typeOfInputCs = f"{project_name}Utils." + type_info
        variables.append(new_variable)
    return variables

def generate_dojo_comm_script(manifest_data, project_name):
    response = input("Do you want the full version? (y/n): ")
    onChain = response.strip().lower() == 'y'
    systems = create_systems(manifest_data["contracts"], project_name)
    classes = generate_classes(systems, classContractTemplate, onChain)

    full_script = ""
    if onChain:
        full_script = dojoContractCommFullTemplate.substitute(classes=classes)
    else:
        full_script = dojoContractCommHalfTemplate.substitute(classes=classes)
    create_file("DojoContractCommunication", "cs", full_script, "scripts")

def generate_utils_script(manifest_data, project_name, repo_name):
    allEnums: List[Enum] = []
    allStructs: List[Struct] = []

    # some structs are used in multiple models and thereofre are duplicated
    
    for models in manifest_data["models"]:
        possibleStructs = []
        for enums in models["members"]:
            if enums["type"] not in type_mapping:
                possibleStructs.append(enums["type"])

        for enums in  models["abi"]:
          if enums["type"] == "enum" and enums["name"].startswith(repo_name):
              newEnum = Enum()
              newEnum.enumName = enums["name"].rsplit("::", 1)[1]
              newEnum.enumOptionsName = [variant["name"] for variant in enums["variants"]]
              allEnums.append(newEnum)

        for structs in models["abi"]:
          if structs["type"] == "struct" and structs["name"].startswith(repo_name) and "members" in structs and structs["name"].rsplit("::", 1)[1] in possibleStructs:
              
              found = False
              for struct in allStructs:
                if struct.structNameDojo == structs["name"].rsplit("::", 1)[1]:
                  found = True
                  break

              if found:
                continue

              newStruct: Struct = Struct()
              newStruct.structNameDojo = structs["name"].rsplit("::", 1)[1]
              newStruct.structNameCs = header_name_format(structs["name"].rsplit("::", 1)[1])
              for members in structs["members"]:
                new_variable = Variable()
                new_variable.nameOfvariableDojo = members["name"]
                new_variable.nameOfvariableCs = var_name_format(members["name"])
                new_variable.typeOfInputDojo = members["type"].rsplit("::", 1)[1]

                if new_variable.typeOfInputDojo in type_mapping:
                    new_variable.typeOfInputCs = type_mapping[new_variable.typeOfInputDojo]
                else:
                    new_variable.typeOfInputCs = f"{header_name_format(project_name)}Utils." + new_variable.typeOfInputDojo
                newStruct.variables.append(new_variable)
              allStructs.append(newStruct)
    
    generated_util_section = ""
    
    structTemplate = Template("""[Serializable]
    public struct ${nameOfStruct}
    {
        ${allFields}
    } 
    """)
    
    enumTemplate = Template("""   [Serializable]
    public enum ${enumName}
    {
        ${allFields}
    }
    """)

    for struct in allStructs:
        allFields = ""
        for variable in struct.variables:
            field = f"public {variable.typeOfInputCs} {variable.nameOfvariableCs};\n"
            allFields += field
        generated_util_section += structTemplate.substitute(allFields=allFields, nameOfStruct=struct.structNameCs) + "\n"

    for enum in allEnums:
        allFields = ",\n".join(enum.enumOptionsName)
        generated_util_section += enumTemplate.substitute(enumName=enum.enumName, allFields=allFields) + "\n"

    update_or_create_script(f"{project_name}Utils", "cs", utilsScriptTemplate.substitute(nameOfProject=project_name, enums=generated_util_section, utilsStatics = utilsStaticTemplate), utilsStaticTemplate + "\n" + generated_util_section, "scripts")

def main():
    # manifest_data = load_manifest('MANIFEST')
    manifest_data = json.loads(MANIFEST)

    repo_name = manifest_data["contracts"][0]["name"].split("::")[0]
    response = input("Project Name?: ")
    project_name = response.strip()

    response = input("Do you want to generate the DojoCommunication script? (y/n): ")
    if response.strip().lower() == 'y':
      generate_dojo_comm_script(manifest_data, project_name)
    print("\n\n\n")
    response = input("Do you want to generate the models scripts? (y/n): ")
    if response.strip().lower() == 'y':
      models = parse_models(manifest_data, type_mapping, project_name, repo_name)
    print("\n\n\n")
    response = input("Do you want to generate the utils scripts? (y/n): ")
    if response.strip().lower() == 'y':
      generate_utils_script(manifest_data, project_name, repo_name)
      
if __name__ == "__main__":
    main()


       