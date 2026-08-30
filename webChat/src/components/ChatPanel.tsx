import { useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import type { ChatMessage } from "../types";

interface ChatPanelProps {
  hasDocument: boolean;
  messages: ChatMessage[];
  asking: boolean;
  error: string | null;
  onSend: (message: string) => void;
}

function ChatPanel({ hasDocument, messages, asking, error, onSend }: ChatPanelProps) {
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight });
  }, [messages, asking]);

  return (
    <div className="h-[70%] bg-surface-container-low shadow-[0_-20px_40px_-10px_rgba(0,0,0,0.5)] flex flex-col relative z-20">
      <div className="h-16 px-lg flex items-center justify-between border-b border-outline-variant/10 bg-surface-container/50 backdrop-blur-md shrink-0">
        <div className="flex items-center gap-sm">
          <span className="material-symbols-outlined text-primary text-[20px]">
            smart_toy
          </span>
          <span className="font-headline-md text-headline-md text-on-surface">
            Assistente
          </span>
        </div>
      </div>

      <div
        ref={scrollRef}
        className="flex-1 overflow-y-auto p-lg flex flex-col gap-lg custom-scrollbar"
      >
        {messages.length === 0 && (
          <div className="flex items-end gap-md self-center my-xl">
            <div className="bg-surface-container-high rounded-full px-lg py-md text-center">
              <p className="font-body-sm text-body-sm text-on-surface-variant">
                {hasDocument
                  ? "Faça uma pergunta sobre o documento."
                  : "Aguardando envio de um documento..."}
              </p>
            </div>
          </div>
        )}

        {messages.map((msg, index) => (
          <MessageBubble key={index} role={msg.role} content={msg.content} />
        ))}

        {asking && (
          <div className="flex items-end gap-md self-center">
            <div className="bg-primary/10 rounded-full px-md py-sm text-center flex items-center gap-sm">
              <span className="material-symbols-outlined text-primary text-[16px] animate-spin">
                refresh
              </span>
              <p className="font-label-sm text-label-sm text-primary">
                Pensando...
              </p>
            </div>
          </div>
        )}
      </div>

      {error && (
        <p className="px-lg pb-sm text-label-sm font-label-sm text-error">
          {error}
        </p>
      )}

      <ChatInput disabled={asking} onSend={onSend} />
    </div>
  );
}

export default ChatPanel;
