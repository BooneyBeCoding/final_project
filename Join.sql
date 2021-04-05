SELECT ird.Title,
    ird.Score,
    ird.subreddit,
	ird.url,
    ird.num-comments,
    ird.body,
    ird.date,
    mlm.Title,
    mlm.WSB?,
    mlm.pos,
    mlm.neutral,
    mlm.neg,
    mlm.compound,
    mlm.predict,
    mlm.correct
INTO Final_Combined_Output
FROM Initial_Reddit_Data AS ird
INNER JOIN MLM_Output AS mlm
ON ird.Title = mlm.Title
