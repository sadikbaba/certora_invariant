methods {
    function totalVotes() external returns(uint256);
    function votesInFavor() external returns(uint256);
    function votesAgainst() external returns(uint256);
}


invariant totalVotesMatch()
    to_mathint(totalVotes()) == votesInFavor() + votesAgainst();
