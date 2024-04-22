#[cfg(test)]
mod test {
    #[test]
    #[available_gas(3000000000)]
    fn test_pedersen() {
        let val = pedersen::pedersen(123, 123);
        println!("{}", val);
    }
}
