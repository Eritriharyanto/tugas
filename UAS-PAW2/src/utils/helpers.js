export function groupByDate(transactions) {
  return transactions.reduce((acc, transaction) => {
    const { date } = transaction;
    if (!acc[date]) acc[date] = [];
    acc[date].push(transaction);
    return acc;
  }, {});
}
