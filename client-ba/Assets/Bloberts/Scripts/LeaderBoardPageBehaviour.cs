using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class LeaderBoardPageBehaviour : Menu
{
    [Header("Simple Board References")]
    [SerializeField] private GameObject _simpleLeaderboard;

    [SerializeField] private GameObject _parentReferencePvE;
    [SerializeField] private GameObject _parentReferencePvP;

    [SerializeField] private GameObject _prefabReference;

    [Header("Complex Board References")]
    [SerializeField] private GameObject _advancedLeaderboard;

    [SerializeField] private List<GameObject> _listOfPodiumPlaces;

    private enum LeaderboardMode
    {
        Simple,
        Advanced
    }
    private enum LeaderboardSort
    {
        Wins,
        Losses,
        MaxConsecutiveWins,
        CurrentConsecutiveWins
    }
    private enum GameMode
    {
        PvE,
        PVP
    }

    [SerializeField] private GameMode _gameModeType;
    [SerializeField] private LeaderboardSort _leaderboardSortType;
    [SerializeField] private LeaderboardMode _leaderboardModeType;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }


    private void OnEnable()
    {
        var sortedListForTotWins = SortByWins(DojoEntitiesStorage.challengeScoreList);

        for (int i = 0; i < _listOfPodiumPlaces.Count; i++)
        {
            if (i >= sortedListForTotWins.Length)
            {
                _listOfPodiumPlaces[i].SetActive(false);
            }
            else
            {
                _listOfPodiumPlaces[i].SetActive(true);
                var blobertCardData = _listOfPodiumPlaces[i].GetComponent<BlobertCardData>();
                blobertCardData.SetBlobertData(sortedListForTotWins[i].dojoBlobertId);
                blobertCardData.SetBlobertWinsText(sortedListForTotWins[i].dojoWins.ToString());
            }
        }
    }

    public static ChallengeScore[] SortByWins(List<ChallengeScore> scores)
    {
        return scores.OrderByDescending(score => score.dojoWins).ToArray();
    }

    public static ChallengeScore[] SortByLosses(List<ChallengeScore> scores)
    {
        return scores.OrderByDescending(score => score.dojoLosses).ToArray();
    }

    public static ChallengeScore[] SortByMaxConsecutiveWins(List<ChallengeScore> scores)
    {
        return scores.OrderByDescending(score => score.dojoMaxConsecutiveWins).ToArray();
    }

    public static ChallengeScore[] SortByCurrentConsecutiveWins(List<ChallengeScore> scores)
    {
        return scores.OrderByDescending(score => score.dojoCurrentConsecutiveWins).ToArray();
    }
}
