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