methods {
    function totalSupply() external returns (uint256) envfree;
}

ghost mathint sumOfBalances {
    init_state axiom sumOfBalances == 0;
}

hook Sload uint256 balance balanceOf[KEY address addr] {
    require sumOfBalances >= to_mathint(balance);
}

invariant totalSupplyEqSumOfBalances()
    to_mathint(totalSupply()) == sumOfBalances;
