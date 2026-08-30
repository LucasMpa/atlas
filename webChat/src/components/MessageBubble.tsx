import type { ChatMessage } from "../types";

function MessageBubble({ role, content }: ChatMessage) {
  if (role === "user") {
    return (
      <div className="flex gap-md max-w-[90%] self-end justify-end">
        <div className="bg-primary text-on-primary rounded-xl rounded-tr-none p-md font-body-md text-body-md whitespace-pre-wrap">
          {content}
        </div>
      </div>
    );
  }

  return (
    <div className="flex gap-md max-w-[90%] self-start">
      <div className="w-8 h-8 rounded-full bg-surface-container-highest flex items-center justify-center shrink-0">
        <span className="material-symbols-outlined text-on-surface text-[16px]">
          smart_toy
        </span>
      </div>
      <div className="bg-surface-container pl-sm rounded-xl rounded-tl-none relative border border-outline-variant/10 shadow-sm">
        <div className="absolute left-0 top-0 bottom-0 w-[4px] bg-primary rounded-l-xl" />
        <div className="p-md text-on-surface font-body-md text-body-md whitespace-pre-wrap ml-1">
          {content}
        </div>
      </div>
    </div>
  );
}

export default MessageBubble;
