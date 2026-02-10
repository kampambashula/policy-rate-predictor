def generate_commentary(predicted_rate, signal, input_df):
    """
    Generates dynamic IMF/Bank of Zambia-style commentary based on macro indicators.
    Inflation is benchmarked against BoZ target of 6-8%.
    """
    commentary_lines = []

    # 1. Policy signal
    commentary_lines.append(f"The model indicates a **{signal}** in the policy rate to approximately {predicted_rate:.2f}%.")

    # 2. Inflation insight (BoZ target 6-8%)
    inflation = input_df['Inflation_Annual'].values[0]
    if inflation > 8:
        commentary_lines.append(
            f"Annual inflation is elevated at {inflation:.1f}%, above the BoZ target range of 6–8%. "
            "This suggests inflationary pressures may warrant a policy rate increase to anchor price stability."
        )
    elif inflation < 6:
        commentary_lines.append(
            f"Annual inflation is low at {inflation:.1f}%, below the BoZ target range of 6–8%. "
            "This indicates price stability, potentially allowing for a hold or modest rate reduction if economic growth is weak."
        )
    else:
        commentary_lines.append(
            f"Inflation is within the BoZ target range at {inflation:.1f}%, supporting a stable monetary policy stance."
        )

    # 3. Liquidity insight
    liquidity = input_df['Actual_Ratio_%'].values[0]
    if liquidity < 20:
        commentary_lines.append(
            f"Liquidity ratio is low at {liquidity:.1f}%, reflecting tight financial conditions. "
            "This may warrant accommodative measures to support banking system stability."
        )
    elif liquidity > 50:
        commentary_lines.append(
            f"Liquidity ratio is high at {liquidity:.1f}%, suggesting ample market liquidity, "
            "which could provide space for monetary tightening if inflationary pressures rise."
        )
    else:
        commentary_lines.append(
            f"Liquidity levels are within normal range at {liquidity:.1f}%."
        )

    # 4. Lending rates insight
    avg_lending = input_df['Average_Lending_Rate'].values[0]
    commentary_lines.append(
        f"Average lending rate is {avg_lending:.2f}%, indicating prevailing credit conditions in the banking sector."
    )

    # 5. Exchange rate perspective
    usd_zmw = input_df['USDZMW'].values[0]
    commentary_lines.append(
        f"The USD/ZMW exchange rate stands at {usd_zmw:.2f}, which could influence imported inflation and overall macro stability."
    )

    # 6. Broad money / monetary expansion
    broad_money = input_df['Broad_Money_M2'].values[0]
    commentary_lines.append(
        f"Broad money (M2) growth is {broad_money:.2f}, reflecting monetary expansion trends that can impact inflation and interest rate policy."
    )

    # 7. Forward-looking policy context
    commentary_lines.append(
        "In conclusion, the model's recommendation integrates inflation trends relative to the BoZ target, "
        "liquidity conditions, and broader macroeconomic indicators, providing a prudent guide for policy rate decisions."
    )

    # Combine lines into Markdown string
    commentary_md = "\n\n".join(commentary_lines)
    return commentary_md
