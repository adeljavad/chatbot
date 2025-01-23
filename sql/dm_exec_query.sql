SELECT TOP 10
    qs.execution_count,
    qs.total_elapsed_time / 1000 AS total_elapsed_time_ms,
    qs.total_worker_time / 1000 AS total_worker_time_ms,
    qs.total_logical_reads,
    qs.total_logical_writes,
    qs.total_physical_reads,
    st.text AS query_text
FROM 
    sys.dm_exec_query_stats qs
CROSS APPLY 
    sys.dm_exec_sql_text(qs.sql_handle) AS st
ORDER BY 
    qs.execution_count DESC;
