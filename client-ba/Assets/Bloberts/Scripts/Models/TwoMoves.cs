using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public enum MoveN
{
    NONE,
    BEAT,
    COUNTER,
    RUSH
}

public class TwoMoves : ModelInstance
{
    [ModelField("id")]
    public FieldElement roundId;

    [ModelField("a")]
    public MoveN b;
    [ModelField("b")]
    public MoveN a;

    private void Start()
    {
        if (DojoEntitiesStatic.currentRoundId != null)
        {
            if (DojoEntitiesStatic.currentRoundId.Hex() == roundId.Hex())
            {
                DojoEntitiesStatic.twoMovesCurrentGame = this;
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
    }
}

