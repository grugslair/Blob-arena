using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;

public class ChallengeScore : ModelInstance
{                     
    #region GeneratedRegion                      
    
    [ModelField("player")]
    public FieldElement dojoPlayer;

    [ModelField("blobert_id")]
    public FieldElement dojoBlobertId;
    [ModelField("wins")]
    public UInt64 dojoWins;

    [ModelField("losses")]
    public UInt64 dojoLosses;

    [ModelField("max_consecutive_wins")]
    public UInt64 dojoMaxConsecutiveWins;

    [ModelField("current_consecutive_wins")]
    public UInt64 dojoCurrentConsecutiveWins;

    #endregion
                              
    private void Start()
    {
        DojoEntitiesStorage.challengeScoreList.Add(this);
    }
                               
    private void Update()
    {
        
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
        //DojoEntitiesStorage
    }
}
