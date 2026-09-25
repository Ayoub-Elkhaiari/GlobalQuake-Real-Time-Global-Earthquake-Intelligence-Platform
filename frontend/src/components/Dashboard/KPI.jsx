export default function KPI({label,value}){return <article className="kpi"><span>{label}</span><strong>{value ?? '—'}</strong></article>}
