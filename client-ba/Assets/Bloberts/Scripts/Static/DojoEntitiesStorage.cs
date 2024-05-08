using Dojo;
using Dojo.Starknet;
using System.Collections.Generic;

public static class DojoEntitiesStorage 
{
    public static WorldManagerData worldManagerData { get; set; }

    //Data about the player
    public static Account currentAccount { get; set; }
    public static List<Blobert> userBloberts = new List<Blobert>();
    public static Blobert userChoosenBlobert { get; set; } 
    //public static BurnerManagerSaver burnerManagerSaver { get; set; }


    // current Lobby data
    public static ChallengeInvite challengeInvite { get; set; }
    public static ChallengeResponse challengeResponse { get; set; }
    public static FieldElement selectedChallengeID { get; set; }


    // this is for the active game
    public static Knockout knockoutCurrentGame { get; set; }
    public static Healths healthsCurrentGame { get; set; }
    public static TwoHashes twoHashesCurrentGame { get; set; }
    public static TwoMoves twoMovesCurrentGame { get; set; }
    public static LastRound lastRoundCurrentGame { get; set; }
    public static FieldElement currentCombatId { get; set; }


    public static Dictionary<string, Knockout> knockoutDict = new Dictionary<string, Knockout>();

    public static Dictionary<string, Healths> healthsDict = new Dictionary<string, Healths>();

    public static Dictionary<string, TwoHashes> twoHashesDict = new Dictionary<string, TwoHashes>();

    public static Dictionary<string, TwoMoves> twoMovesDict = new Dictionary<string, TwoMoves>();

    public static Dictionary<string, Blobert> allBlobertDict = new Dictionary<string, Blobert>();

    public static Dictionary<string, ChallengeResponse> challengeResponseDict = new Dictionary<string, ChallengeResponse>();
    public static Dictionary<string,ChallengeInvite> challengeInvitesDict = new Dictionary<string, ChallengeInvite>();


    public static HashSet<ChallengeInvite> userReceivedChallengeInvites = new HashSet<ChallengeInvite>();
    
}
