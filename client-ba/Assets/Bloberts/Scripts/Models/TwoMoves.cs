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

    #region GeneratedRegion 

    [ModelField("id")]
    public FieldElement dojoId;
    


    [ModelField("a")]
    public BlobertUtils.MoveN dojoA;
    


    [ModelField("b")]
    public BlobertUtils.MoveN dojoB;
    

    #endregion


    private void Start()
    {
        if (DojoEntitiesStorage.currentCombatId != null)
        {
            if (DojoEntitiesStorage.currentCombatId.Hex() == dojoId.Hex())
            {
                DojoEntitiesStorage.twoMovesCurrentGame = this;
            }
        }

        if (DojoEntitiesStorage.currentCombatId == null)
        {
            return;
        }

        if (DojoEntitiesStorage.currentCombatId.Hex() == dojoId.Hex())
        {
            DojoEntitiesStorage.twoMovesCurrentGame = this;

            if (UiReferencesStatic.battlePageBehaviour != null)
            {
                UiReferencesStatic.battlePageBehaviour.CallFromDataToUpdate();
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (DojoEntitiesStorage.currentCombatId == null)
        {
            return;
        }

        if (DojoEntitiesStorage.currentCombatId.Hex() != dojoId.Hex())
        {
            return;
        }

        if (UiReferencesStatic.battlePageBehaviour != null)
        {
            UiReferencesStatic.battlePageBehaviour.CallFromDataToUpdate();
        }
    }
}
