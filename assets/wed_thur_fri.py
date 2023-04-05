import z3

flag = [z3.Int(f"f_{i}") for i in range(34)]

solver = z3.Solver()

for i in range(34):
  solver.add(flag[i]<=256)
  solver.add(flag[i]>=0)

solver.add(
    (
        (((flag[7] - flag[5] * flag[6] * flag[2] * flag[8]) - flag[0xB]) - flag[9])
        + flag[1]
        + flag[4]
        + flag[3]
    )
    - flag[10]
    == -0x31E4A76
)

solver.add(
    (
        flag[0xC] * flag[7]
        + (
            (((flag[3] - flag[4]) - flag[6]) + flag[9] + flag[10] * flag[0xB] * flag[8])
            - flag[2]
        )
        + flag[5]
        == 0x45C0B
    )
)

solver.add(
    flag[8]
    + (
        (((flag[3] - flag[7] * flag[0xC]) - flag[0xD]) + flag[4] * flag[10])
        - flag[6] * flag[9] * flag[5]
    )
    + flag[0xB]
    == -0xC29D9
)

solver.add(
    (
        (
            (
                (((flag[0xC] - flag[0xB] * flag[7]) + flag[4]) - flag[9])
                - flag[6] * flag[5]
            )
            - flag[0xE]
        )
        - flag[10] * flag[0xD] * flag[8]
        == -0x469FB
    )
)
solver.add(
    flag[9] * flag[10] * flag[8]
    + (
        (
            ((flag[6] + flag[7] + flag[0xE] + flag[0xD]) - flag[0xC])
            - flag[0xB] * flag[0xF]
        )
        - flag[5]
    )
    == 0xA2CF4
)

solver.add(
    flag[0xE]
    + (
        (
            (
                ((flag[0xD] + flag[0xB]) - flag[10])
                + flag[0x10] * flag[0xF]
                + flag[8] * flag[6]
            )
            - flag[7]
        )
        - flag[9]
    )
    + flag[0xC]
    == 0x266D
)

solver.add(
    (
        (
            (
                (
                    ((flag[0xB] - flag[8]) + flag[0xD] * flag[0x10] + flag[7])
                    - flag[0x11]
                )
                - flag[0xE]
            )
            - flag[9]
        )
        + flag[0xF] * flag[10]
    )
    - flag[0xC]
    == 0x2682
)


solver.add(
    (
        ((((flag[9] - flag[0x12]) - flag[8]) + flag[0xC]) - flag[0xF])
        + flag[0x10]
        + flag[0xD] * flag[0xE] * flag[0xB]
        + flag[0x11]
    )
    - flag[10]
    == 0x48638
)
solver.add(
    (
        (
            ((flag[0x10] * flag[0x12] * flag[0xD] * flag[0xB] - flag[0x11]) - flag[10])
            + flag[9]
            + flag[0xC] * flag[0xF]
        )
        - flag[0x13]
    )
    - flag[0xE]
    == 0xA749BB
)

solver.add(
    (
        (
            (
                (
                    (
                        (flag[0x14] + flag[0xC])
                        - flag[0x13] * flag[0xF] * flag[0x12] * flag[0xE]
                    )
                    + flag[0x10]
                )
                - flag[0xD]
            )
            + flag[0x11]
        )
        - flag[0xB]
    )
    - flag[10]
    == -0x3ED657C
)
solver.add(
    flag[0x14] * flag[0x11]
    + ((flag[0x10] - flag[0x13]) - flag[0xF])
    + flag[0xD] * flag[0xB]
    + flag[0x12]
    + flag[0xC] * flag[0x15]
    + flag[0xE]
    == 0x341C
)

solver.add(
    flag[0x15] * flag[0xD]
    + (((flag[0xF] * flag[0x11] - flag[0x14]) - flag[0xC]) - flag[0xE] * flag[0x13])
    + flag[0x16]
    + flag[0x10] * flag[0x12]
    == 0x1221
)

solver.add(
    flag[0x17] * flag[0x11]
    + (
        (
            (((flag[0x15] + flag[0x13] * flag[0xD]) - flag[0x16]) - flag[0x10])
            + flag[0x12]
            + flag[0x14]
            + flag[0xF]
        )
        - flag[0xE]
    )
    == 0x191C
)
solver.add(
    (
        (
            (flag[0x17] + flag[0xE] * flag[0x10] + flag[0x14] * flag[0xF])
            - flag[0x15] * flag[0x12]
        )
        + flag[0x18] * flag[0x13]
    )
    - flag[0x11] * flag[0x16]
    == 0x1EAB
)

solver.add(
    flag[0x11]
    + (
        (
            flag[0x10]
            + flag[0x19]
            + flag[0x15]
            + flag[0x16]
            + flag[0x18]
            + flag[0x12]
            + flag[0x17] * flag[0x14]
        )
        - flag[0xF]
    )
    + flag[0x13]
    == 0xBB5
)

solver.add(
    flag[0x12] * flag[0x13] * flag[0x16]
    + (
        (
            ((flag[0x17] * flag[0x11] + flag[0x19] * flag[0x14]) - flag[0x10])
            + flag[0x15] * flag[0x1A]
        )
        - flag[0x18]
    )
    == 0x53999
)

solver.add(
    (
        flag[0x17]
        + (
            (
                (
                    flag[0x11] * flag[0x18]
                    + flag[0x19] * flag[0x16] * flag[0x1B]
                    + flag[0x1A]
                    + flag[0x14]
                )
                - flag[0x15]
            )
            - flag[0x12] * flag[0x13]
        )
        == 0x3B633
    )
)

solver.add(
    flag[0x12]
    + (
        (
            (
                (((flag[0x15] * flag[0x19] + flag[0x16]) - flag[0x1C]) - flag[0x13])
                - flag[0x14] * flag[0x1B] * flag[0x1A]
            )
            + flag[0x18]
        )
        - flag[0x17]
    )
    == -0x6A254
)

solver.add(
    flag[0x14]
    + (
        (
            (
                (((flag[0x1D] + flag[0x19] + flag[0x13]) - flag[0x18]) - flag[0x15])
                - flag[0x17]
            )
            + flag[0x1C]
            + flag[0x1B]
        )
        - flag[0x1A] * flag[0x16]
    )
    == -0x135D
)

solver.add(
    (
        (
            (
                (
                    (flag[0x1A] + flag[0x17] * flag[0x16] + flag[0x1E] + flag[0x15])
                    - flag[0x1D]
                )
                + flag[0x14]
            )
            - flag[0x19] * flag[0x18]
        )
        - flag[0x1B]
    )
    - flag[0x1C]
    == -0x659
)
solver.add(
    (
        (
            (
                (
                    (
                        (
                            (((flag[0x17] + flag[0x1E]) - flag[0x18]) + flag[0x19])
                            - flag[0x1D]
                        )
                        - flag[0x1F]
                    )
                    - flag[0x15]
                )
                + flag[0x1A]
            )
            - flag[0x1B]
        )
        + flag[0x16]
    )
    - flag[0x1C]
    == -0x90
)

solver.add(
    (
        (
            (
                (
                    (
                        (((flag[0x1F] - flag[0x1A]) - flag[0x19]) - flag[0x17])
                        + flag[0x1E]
                    )
                    - flag[0x1C]
                )
                + flag[0x1D]
            )
            - flag[0x1B]
        )
        - flag[0x16]
    )
    - flag[0x18] * flag[0x20]
    == -0x1B59
)
solver.add(
    (
        (
            (
                (
                    ((flag[0x19] - flag[0x17] * flag[0x1F]) + flag[0x1B])
                    - flag[0x20] * flag[0x1A]
                )
                + flag[0x1E]
            )
            - flag[0x1D] * flag[0x18]
        )
        + flag[0x21]
    )
    - flag[0x1C]
    == -0x494B
)
print("Check 1")
print(solver.check())
m = solver.model()
print("Check 2")
out = [chr(m.evaluate(flag[i]).as_long()) for i in range(34)]

print("".join(out))
