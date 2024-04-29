using Dojo.Starknet;
using System;
using System.Collections.Generic;

public static class DojoEntitiesStatic 
{
    //public static 
    public static Account currentAccount { get; set; }
    public static Blobert userBlobertData { get; set; }
    public static BurnerManagerSaver burnerManagerSaver { get; set; }



    public static Knockout knockoutCurrentGame { get; set; }
    public static Healths healthsCurrentGame { get; set; }
    public static TwoHashes twoHashesCurrentGame { get; set; }
    public static TwoMoves twoMovesCurrentGame { get; set; }
    public static LastRound lastRoundCurrentGame { get; set; }

    public static FieldElement currentRoundId { get; set; }


    public static Dictionary<string, TwoHashes> twoHashesDict = new Dictionary<string, TwoHashes>();

    public static Dictionary<string, TwoMoves> twoMovesDict = new Dictionary<string, TwoMoves>();

    public static Dictionary<string, Blobert> allBlobertDict = new Dictionary<string, Blobert>();

    public static List<Knockout> knockoutsList = new List<Knockout>();
    public static List<Healths> healthsList = new List<Healths>();
}