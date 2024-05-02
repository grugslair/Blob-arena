using Dojo.Starknet;
using System;
using System.Numerics;
using System.Runtime.InteropServices;

public static class BlobertUtils
{
    [Serializable]
    public struct U256
    {
        public BigInteger high;
        public BigInteger low;
    }

    [Serializable]
    public struct Vec2
    {
        public UInt32 x;
        public UInt32 y;
    }

    public enum Move
    {
        Beat = 0,
        Counter = 1,
        Rush = 2
    }


    [Serializable]
    public struct Traits
    {
        public Background background;
        public Armour armour;
        public Mask mask;
        public Jewelry jewelry;
        public Weapon weapon;
    }

    [Serializable]
    public enum Jewelry
    {
        Amulet,
        BronzeRing,
        GoldRing,
        Necklace,
        Pendant,
        PlatinumRing,
        SilverRing,
        TitaniumRing,
    }
    public static string TraitJewelryToFileName(Jewelry trait)
    {
        switch (trait)
        {
            case Jewelry.Amulet:
                return "amulet";
            case Jewelry.BronzeRing:
                return "bronze_ring";
            case Jewelry.GoldRing:
                return "gold_ring";
            case Jewelry.Necklace:
                return "necklace";
            case Jewelry.Pendant:
                return "pendant";
            case Jewelry.PlatinumRing:
                return "platinum_ring";
            case Jewelry.SilverRing:
                return "silver_ring";
            case Jewelry.TitaniumRing:
                return "titanium_ring";
            default:
                return "";
        }
    }


    [Serializable]
    public enum Armour
    {
        SheepsWool,
        Kigurumi,
        DivineRobeDark,
        DivineRobe,
        DojoRobe,
        HolyChestplate,
        DemonHusk,
        LeatherArmour,
        LeopardSkin,
        LinenRobe,
        LordsArmor,
        SecretTattoo,
        Chainmail,
        Suit,
        Underpants,
        WenShirt,
        WsbTankTop,
    }
    public static string TraitArmourToFileName(Armour trait)
    {
        switch (trait)
        {
            case Armour.SheepsWool:
                return "sheeps_wool";
            case Armour.Kigurumi:
                return "kigurumi";
            case Armour.DivineRobeDark:
                return "divine_robe_dark";
            case Armour.DivineRobe:
                return "divine_robe";
            case Armour.DojoRobe:
                return "dojo_robe";
            case Armour.HolyChestplate:
                return "holy_chestplate";
            case Armour.DemonHusk:
                return "demon_husk";
            case Armour.LeatherArmour:
                return "leather_armour";
            case Armour.LeopardSkin:
                return "leopard_skin";
            case Armour.LinenRobe:
                return "linen_robe";
            case Armour.LordsArmor:
                return "lords_armor";
            case Armour.SecretTattoo:
                return "secret_tattoo";
            case Armour.Chainmail:
                return "chainmail";
            case Armour.Suit:
                return "suit";
            case Armour.Underpants:
                return "underpants";
            case Armour.WenShirt:
                return "wen_shirt";
            case Armour.WsbTankTop:
                return "wsb_tank_top";
            default:
                return "";
        }
    }


    [Serializable]
    public enum Mask
    {
        Blobert,
        Doge,
        Dojo,
        Ducks,
        Kevin,
        Milady,
        Pepe,
        Pudgy,
        _3dGlasses,
        _1337Skulls,
        AncientHelm,
        Bane,
        BraavosHelm,
        Bulbhead,
        DealWithItGlasses,
        DemonCrown,
        DivineHood,
        Ekubo,
        HyperlootCrown,
        InfluenceHelmet,
        LordsHelm,
        Nostrahat,
        NounsGlasses,
        PopeHat,
        TaprootWizardHat,
        WifHat,
    }
    public static string TraitMaskToFileName(Mask trait)
    {
        switch (trait)
        {
            case Mask.Blobert:
                return "blobert";
            case Mask.Doge:
                return "doge";
            case Mask.Dojo:
                return "dojo";
            case Mask.Ducks:
                return "ducks";
            case Mask.Kevin:
                return "kevin";
            case Mask.Milady:
                return "milady";
            case Mask.Pepe:
                return "pepe";
            case Mask.Pudgy:
                return "pudgy";
            case Mask._3dGlasses:
                return "3d_glasses";
            case Mask._1337Skulls:
                return "1337_skulls";
            case Mask.AncientHelm:
                return "ancient_helm";
            case Mask.Bane:
                return "bane";
            case Mask.BraavosHelm:
                return "braavos_helm";
            case Mask.Bulbhead:
                return "bulbhead";
            case Mask.DealWithItGlasses:
                return "deal_with_it_glasses";
            case Mask.DemonCrown:
                return "demon_crown";
            case Mask.DivineHood:
                return "divine_hood";
            case Mask.Ekubo:
                return "ekubo";
            case Mask.HyperlootCrown:
                return "hyperloot_crown";
            case Mask.InfluenceHelmet:
                return "influence_helmet";
            case Mask.LordsHelm:
                return "lords_helm";
            case Mask.Nostrahat:
                return "nostrahat";
            case Mask.NounsGlasses:
                return "nouns_glasses";
            case Mask.PopeHat:
                return "pope_hat";
            case Mask.TaprootWizardHat:
                return "taproot_wizard_hat";
            case Mask.WifHat:
                return "wif_hat";
            default:
                return "";
        }
    }


    [Serializable]
    public enum Weapon
    {
        AlgorithmicAegis,
        ArgentShield,
        Balloons,
        BannerOfAnger,
        BannerOfBrilliance,
        BannerOfDetection,
        BannerOfEnlightenment,
        BannerOfFury,
        BannerOfGiants,
        BannerOfPerfection,
        BannerOfPower,
        BannerOfProtection,
        BannerOfRage,
        BannerOfReflection,
        BannerOfSkill,
        BannerOfTheFox,
        BannerOfTheTwins,
        BannerOfTitans,
        BannerOfTonyHawk,
        BannerOfVitriol,
        Banner,
        Briq,
        Calculator,
        DevvingForTheDistracted,
        DiamondHands,
        DopeUzi,
        GhostWand,
        Grimoire,
        GrugsClub,
        JediswapSaber,
        Katana,
        LordsBanner,
        LsHasNoChill,
        Mandolin,
        SignIso,
        SignatureBanner,
        SithswapSaber,
        Spaghetti,
        Squid,
        StarkMagic,
        StarkShield,
        Stool,
        Warhammer,
    }
    public static string TraitWeaponToFileName(Weapon trait)
    {
        switch (trait)
        {
            case Weapon.AlgorithmicAegis:
                return "algorithmic_aegis";
            case Weapon.ArgentShield:
                return "argent_shield";
            case Weapon.Balloons:
                return "balloons";
            case Weapon.BannerOfAnger:
                return "banner_of_anger";
            case Weapon.BannerOfBrilliance:
                return "banner_of_brilliance";
            case Weapon.BannerOfDetection:
                return "banner_of_detection";
            case Weapon.BannerOfEnlightenment:
                return "banner_of_enlightenment";
            case Weapon.BannerOfFury:
                return "banner_of_fury";
            case Weapon.BannerOfGiants:
                return "banner_of_giants";
            case Weapon.BannerOfPerfection:
                return "banner_of_perfection";
            case Weapon.BannerOfPower:
                return "banner_of_power";
            case Weapon.BannerOfProtection:
                return "banner_of_protection";
            case Weapon.BannerOfRage:
                return "banner_of_rage";
            case Weapon.BannerOfReflection:
                return "banner_of_reflection";
            case Weapon.BannerOfSkill:
                return "banner_of_skill";
            case Weapon.BannerOfTheFox:
                return "banner_of_the_fox";
            case Weapon.BannerOfTheTwins:
                return "banner_of_the_twins";
            case Weapon.BannerOfTitans:
                return "banner_of_titans";
            case Weapon.BannerOfTonyHawk:
                return "banner_of_tony_hawk";
            case Weapon.BannerOfVitriol:
                return "banner_of_vitriol";
            case Weapon.Banner:
                return "banner";
            case Weapon.Briq:
                return "briq";
            case Weapon.Calculator:
                return "calculator";
            case Weapon.DevvingForTheDistracted:
                return "devving_for_the_distracted";
            case Weapon.DiamondHands:
                return "diamond_hands";
            case Weapon.DopeUzi:
                return "dope_uzi";
            case Weapon.GhostWand:
                return "ghost_wand";
            case Weapon.Grimoire:
                return "grimoire";
            case Weapon.GrugsClub:
                return "grugs_club";
            case Weapon.JediswapSaber :
                return "jediswap_saber";
            case Weapon.Katana:
                return "katana";
            case Weapon.LordsBanner:
                return "lords_banner";
            case Weapon.LsHasNoChill:
                return "ls_has_no_chill";
            case Weapon.Mandolin:
                return "mandolin";
            case Weapon.SignIso:
                return "sign_iso";
            case Weapon.SignatureBanner:
                return "signature_banner";
            case Weapon.SithswapSaber:
                return "sithswap_saber";
            case Weapon.Spaghetti:
                return "spaghetti";
            case Weapon.Squid:
                return "squid";
            case Weapon.StarkMagic:
                return "stark_magic";
            case Weapon.StarkShield:
                return "stark_shield";
            case Weapon.Stool:
                return "stool";
            case Weapon.Warhammer:
                return "warhammer";
            default:
                return "";
        }
    }


    [Serializable]
    public enum Background
    {
        AvnuBlue,
        Blue,
        CryptsAndCaverns,
        FibrousFrame,
        Green,
        Holo,
        Orange,
        Purple,
        RealmsDark,
        Realms,
        Terraforms,
        Tulip,
    }

    [Serializable]
    public struct Stats
    {
        public byte attack;
        public byte defense;
        public byte speed;
        public byte strength;
    }

    [DllImport("__Internal")]
    public static extern string PedersenFunction(int value1Ptr, int value2Ptr);

    public static string emptyFieldElement = "0x0000000000000000000000000000000000000000000000000000000000000000";

    public static BigInteger HexToBigInt(string hex)
    {
        // Check if hex starts with "0x" and remove it
        if (hex.StartsWith("0x", StringComparison.OrdinalIgnoreCase))
        {
            hex = hex.Substring(2);
        }
        return BigInteger.Parse("0" + hex, System.Globalization.NumberStyles.HexNumber);
    }

    public static string Address0sFix(string inputHash)
    {
        const int requiredLength = 66;

        if (!inputHash.StartsWith("0x"))
        {
            inputHash = "0x" + inputHash;
        }

        int missingZeros = requiredLength - inputHash.Length;

        if (missingZeros > 0)
        {
            inputHash = "0x" + new string('0', missingZeros) + inputHash.Substring(2);
        }

        return inputHash;
    }

}
