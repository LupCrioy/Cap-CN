import { Navigate, useSearchParams } from "@solidjs/router";

export default function 设置() {
	const [searchParams] = useSearchParams();
	const page = (searchParams.page as string) || "general";

	return <Navigate href={page} />;
}
