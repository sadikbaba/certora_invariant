// SPDX-License-Identifier: MIT
pragma solidity 0.8.25;

contract simpleEquation {
    // 2x+5=17

    /* we can get the answer by
    * collect like term
    * 2x = 17 - 5
    * 2x = 12
    * divide both side by 2
    * x = 6
    *
    * 2 * 6 + 5 = 17
    * we can verify this using certora
    */
    function findX(uint256 x) external pure returns (bool) {
        return (2 * x + 5 == 17);
    }

    // 3x−4=2x+6
    function solve(uint256 x) external pure returns (bool) {
        return (3 * x - 4) == (2 * x + 6);
    }

    // 4x−3=2x+9

    function simplify(uint256 x) external pure returns (bool) {
        return (4 * x - 3) == (2 * x + 9);
    }
}
