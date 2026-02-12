methods {
    function findX(uint256) external returns (bool) envfree;
    function solve(uint256) external returns (bool) envfree;
    function simplify(uint256) external returns (bool)envfree;
}

rule simpleEquation() {
    // var
    uint256 x;
    uint256 y;
    uint256 z;

    satisfy findX(x) == true;
    satisfy solve(y) == true;
    satisfy simplify(z) == true;

    assert x == 6;
    assert y == 10;
    assert z == 6;
}
